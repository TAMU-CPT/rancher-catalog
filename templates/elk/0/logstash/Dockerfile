# https://github.com/elastic/logstash-docker
FROM docker.elastic.co/logstash/logstash:5.4.0

# Add your logstash plugins setup here
# Example: RUN logstash-plugin install logstash-filter-json
ADD logstash.yml /usr/share/logstash/config/logstash.yml
ADD logstash.conf /usr/share/logstash/pipeline/logstash.conf
