# https://github.com/elastic/elasticsearch-docker
FROM docker.elastic.co/elasticsearch/elasticsearch:5.4.0

# Add your elasticsearch plugins setup here
RUN elasticsearch-plugin install analysis-icu && \
	echo 'discovery.type: single-node' >> config/elasticsearch.yml  && \
	echo 'xpack.security.enabled: false' >> config/elasticsearch.yml && \
	echo 'xpack.monitoring.enabled: false' >> config/elasticsearch.yml && \
	echo 'xpack.ml.enabled: false' >> config/elasticsearch.yml && \
	echo 'xpack.graph.enabled: false' >> config/elasticsearch.yml && \
	echo 'xpack.watcher.enabled: false' >> config/elasticsearch.yml
