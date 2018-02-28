Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:           logback
Version:        1.1.2
Release:        alt1_5jpp8
Summary:        A Java logging library
License:        LGPLv2 or EPL
URL:            http://logback.qos.ch/
Source0:        http://logback.qos.ch/dist/%{name}-%{version}.tar.gz
# use antrun-plugin instead of gmaven
Patch0:         %{name}-1.0.10-antrunplugin.patch
# servlet 3.1 support
Patch1:         %{name}-1.1.2-servlet.patch
Patch2:         %{name}-1.1.2-jetty9.3.0.patch

# Java dependencies

# Required libraries
BuildRequires: mvn(javax.mail:mail)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires: mvn(org.codehaus.janino:janino)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-util)
BuildRequires: mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires: mvn(org.fusesource.jansi:jansi)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-ext)

%if %{?fedora} > 21
# use groovy 2.x
BuildRequires: mvn(org.codehaus.groovy:groovy-all)
BuildRequires: mvn(org.ow2.asm:asm-all)
%else
# use groovy 1.8.9
BuildRequires: mvn(org.codehaus.groovy:groovy:1.8.9)
BuildRequires: mvn(asm:asm-all)
%endif
# groovy-all embedded libraries
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(org.slf4j:slf4j-nop)

# test deps
%if 0
BuildRequires: mvn(com.h2database:h2:1.2.132)
BuildRequires: mvn(dom4j:dom4j:1.6.1)
BuildRequires: mvn(hsqldb:hsqldb:1.8.0.7)
BuildRequires: mvn(mysql:mysql-connector-java:5.1.9)
BuildRequires: mvn(postgresql:postgresql:8.4-701.jdbc4)
BuildRequires: mvn(org.easytesting:fest-assert:1.2)
BuildRequires: mvn(org.mockito:mockito-core:1.9.0)
BuildRequires: mvn(org.slf4j:integration:1.7.5)
BuildRequires: mvn(org.slf4j:jul-to-slf4j:1.7.5)
BuildRequires: mvn(org.slf4j:log4j-over-slf4j:1.7.5)
BuildRequires: mvn(org.slf4j:slf4j-api:1.7.5:test-jar)
BuildRequires: mvn(org.slf4j:slf4j-ext:1.7.5)
BuildRequires: mvn(com.icegreen:greenmail:1.3)
BuildRequires: mvn(org.subethamail:subethasmtp:2.1.0)
# mvn(ch.qos.logback:logback-core:%%{version}:test-jar)
%endif

# antrun plugin deps
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.felix:org.apache.felix.main)
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
#BuildRequires: maven-source-plugin

BuildArch:     noarch
Source44: import.info

%description
Logback is intended as a successor to the popular log4j project. At present
time, logback is divided into three modules, logback-core, logback-classic
and logback-access.

The logback-core module lays the groundwork for the other two modules. The
logback-classic module can be assimilated to a significantly improved
version of log4j. Moreover, logback-classic natively implements the SLF4J
API so that you can readily switch back and forth between logback and other
logging frameworks such as log4j or java.util.logging (JUL).

The logback-access module integrates with Servlet containers, such as
Tomcat and Jetty, to provide HTTP-access log functionality. Note that you
could easily build your own module on top of logback-core.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for the Logback library

%package access
Group: Development/Java
Summary:       Logback-access module for Servlet integration

%description access
The logback-access module integrates with Servlet containers, such as Tomcat
and Jetty, to provide HTTP-access log functionality. Note that you could
easily build your own module on top of logback-core. 

%package examples
Group: Development/Java
Summary:       Logback Examples Module

%description examples
logback-examples module.

%prep
%setup -q
# Clean up
find . -name "*.class" -delete
find . -name "*.cmd" -delete
find . -name "*.jar" -delete

%patch0 -p0
sed -i 's|source="1.5" target="1.5"|source="1.6" target="1.6"|' %{name}-classic/pom.xml
%patch1 -p1
%patch2 -p1

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :gmaven-plugin %{name}-classic

# Clean up the documentation
sed -i 's/\r//' LICENSE.txt README.txt docs/*.* docs/*/*.* docs/*/*/*.*
sed -i 's#"apidocs#"%{_javadocdir}/%{name}#g' docs/*.html
rm -rf docs/apidocs docs/project-reports docs/testapidocs docs/project-reports.html
rm -f docs/manual/.htaccess docs/css/site.css # Zero-length file

sed -i 's#<artifactId>groovy-all</artifactId#<artifactId>groovy</artifactId#' $(find . -name "pom.xml")

# Fix build with groovy2
%if %{?fedora} > 21
sed -i 's#groupId>asm#groupId>org.ow2.asm#' %{name}-classic/pom.xml
sed -i 's#artifactId>groovy#artifactId>groovy-all#' %{name}-classic/pom.xml
%endif

# force tomcat apis
sed -i 's#<groupId>javax.servlet#<groupId>org.apache.tomcat#' $(find . -name "pom.xml")
sed -i 's#<artifactId>servlet-api#<artifactId>tomcat-servlet-api#' $(find . -name "pom.xml")
sed -i 's#javax.servlet.*;version="2.5"#javax.servlet.*;version="3.1"#' %{name}-access/pom.xml
sed -i 's#<version>2.5</version>#<version>${tomcat.version}</version>#' pom.xml

sed -i 's#<version>1.2.14</version>#<version>1.2.17</version>#' %{name}-examples/pom.xml

rm -r %{name}-*/src/test/java/*
# remove test deps
# ch.qos.logback:logback-core:test-jar
%pom_xpath_remove "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:type = 'test-jar']"

while read f
do

%pom_xpath_remove "pom:project/pom:dependencies/pom:dependency[pom:type = 'test-jar']" ${f}

done << EOF
%{name}-access/pom.xml
%{name}-classic/pom.xml
EOF

while read f
do

%pom_xpath_remove "pom:project/pom:dependencies/pom:dependency[pom:scope = 'test']" ${f}

done << EOF
pom.xml
%{name}-access/pom.xml
%{name}-classic/pom.xml
%{name}-core/pom.xml
EOF

# bundle-test-jar
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-jar-plugin']/pom:executions" %{name}-access
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-jar-plugin']/pom:executions" %{name}-classic
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-jar-plugin']/pom:executions" %{name}-core

# com.oracle:ojdbc14:10.2.0.1 com.microsoft.sqlserver:sqljdbc4:2.0
%pom_xpath_remove "pom:project/pom:profiles/pom:profile[pom:id = 'host-orion']" %{name}-access
%pom_xpath_remove "pom:project/pom:profiles" %{name}-classic

%pom_xpath_remove "pom:project/pom:profiles/pom:profile[pom:id = 'javadocjar']"

# disable for now
%pom_disable_module logback-site

%pom_xpath_remove "pom:build/pom:extensions"

%build

%mvn_package ":%{name}-access" access
%mvn_package ":%{name}-examples" examples
# unavailable test dep maven-scala-plugin
# slf4jJAR and org.apache.felix.main are required by logback-examples modules for maven-antrun-plugin
%mvn_build -f -- \
  -Dslf4jJAR=$(build-classpath slf4j/api) \
  -Dorg.apache.felix:org.apache.felix.main:jar=$(build-classpath felix/org.apache.felix.main)

%install
%mvn_install

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/examples
cp -r %{name}-examples/pom.xml %{name}-examples/src %{buildroot}%{_datadir}/%{name}-%{version}/examples

%files -f .mfiles
%doc README.txt docs/*
%doc LICENSE.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%files access -f .mfiles-access
%doc LICENSE.txt

%files examples -f .mfiles-examples
%doc LICENSE.txt
%{_datadir}/%{name}-%{version}

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_5jpp8
- java 8 mass update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt2_2jpp7
- fixed build (use java6 due to reflection API change)

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt1_2jpp7
- fc update

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_3jpp7
- new version

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.27-alt1_1jpp6
- new version

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt2_2jpp6
- build with compat slf4j15

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt1_2jpp6
- new version

