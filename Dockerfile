FROM felixgondwe/sgd:18.5.0

#copy code
WORKDIR /app
COPY . /app

RUN pip install -U setuptools
RUN pip install -U Celery=="3.1.20"
RUN pip install -r /app/requirements.txt
RUN python /app/setup.py develop
RUN npm install
RUN npm install -g grunt-cli

ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock
RUN /bin/bash -l -c "bundle install"
