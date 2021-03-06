vcl 4.0;

acl purgers {
    "127.0.0.1";
    "172.16.0.0/12";
}

backend default {
    .host = "127.0.0.1";
    .port = "8080";
    .connect_timeout = 300s;
    .first_byte_timeout = 300s;
}

sub vcl_recv {
    # pass POSTs so varnish doesn't transform into GET
    if (req.method == "POST") {
        return (pass);
    }
    if (req.method == "PURGE") {
        if (!client.ip ~ purgers) {
            return (synth(405));
        }
        return (purge);
    }

    # redirect @ -> www
    if (req.http.host == "yeastgenome.org") {
        return (synth(750, ""));
    }

    # force HTTPS
    if (req.http.X-Forwarded-Proto !~ "(?i)https" && req.url !~ "healthcheck$" && client.ip != "127.0.0.1") {
        return (synth(750, ""));
    }

    unset req.http.Cookie;
    set req.http.host = "www.yeastgenome.org";

    # don't cache healthcheck
    if (req.url ~ "healthcheck$") {
        return (pass);
    }
}

sub vcl_backend_response {
    if (beresp.status != 200) {
        set beresp.ttl = 15s;
        return (deliver);
    }

    set beresp.ttl = 23.75h;
    set beresp.grace = 30s;

    unset beresp.http.Server;
    unset beresp.http.Vary;
}

sub vcl_deliver {
    unset resp.http.Server;
    unset resp.http.Via;
    unset resp.http.X-Varnish;
}

sub vcl_purge {
    set req.method = "GET";
    return (restart);
}

sub vcl_synth {
    if (resp.status == 750) {
        set resp.http.Location = "https://www.yeastgenome.org" + req.url;
        set resp.status = 302;
        return (deliver);
    }
}
