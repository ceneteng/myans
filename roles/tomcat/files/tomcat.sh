
mkdir /opt/tomcat
tar xzvf /tmp/apache-tomcat-8*tar.gz -C /opt/tomcat --strip-components=1
chgrp -R tomcat /opt/tomcat
chmod -R g+r /opt/tomcat/conf
chmod g+x /opt/tomcat/conf
chown -R tomcat /opt/tomcat/webapps/ /opt/tomcat/work/ /opt/tomcat/temp/ /opt/tomcat/logs/
update-java-alternatives -l

systemctl daemon-reload
systemctl start tomcat
systemctl status tomcat

