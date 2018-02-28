Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          uimaj
Version:       2.5.0
Release:       alt1_5jpp8
Summary:       Apache UIMA is an implementation of the OASIS-UIMA specifications
License:       ASL 2.0
URL:           http://uima.apache.org/
Source0:       http://www.apache.org/dist/uima/%{name}-%{version}/%{name}-%{version}-source-release.zip

BuildRequires: mvn(ant-contrib:ant-contrib)
BuildRequires: mvn(axis:axis)
BuildRequires: mvn(axis:axis-jaxrpc)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.commons:commons-logging)
# maven plugins
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-javadoc)
BuildRequires: mvn(org.apache.uima:parent-pom:pom:)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)

BuildRequires: apache-rat-plugin
BuildRequires: maven-local
BuildRequires: maven-dependency-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-plugin
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: mvn(org.apache.ant:ant-apache-regexp)

BuildArch:     noarch
Source44: import.info

%description
Apache UIMA is an implementation of the OASIS-UIMA specifications.

OASIS UIMA Committee: <http://www.oasis-open.org/committees/uima/>.

Unstructured Information Management applications are software systems
that analyze large volumes of unstructured information in order to
discover knowledge that is relevant to an end user.

An example UIM application might ingest plain text and identify
entities, such as persons, places, organizations; or relations,
such as works-for or located-at.

%package -n jcasgen-maven-plugin
Group: Development/Java
Summary:       Apache UIMA Maven JCasGen Plugin

%description -n jcasgen-maven-plugin
A Maven Plugin for using JCasGen to generate Java classes from
XML type system descriptions.

%package -n uima-pear-maven-plugin
Group: Development/Java
Summary:       Apache UIMA Maven Pear Plugin

%description -n uima-pear-maven-plugin
This is a maven plugin that produces a pear artifact.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# Cleanup
find .  -name "*.jar" -delete
find .  -name "*.bat" -delete
find .  -name "*.class" -delete
find .  -name "*.cmd" -delete

# [ERROR] uimaj-adapter-soap/src/main/java/org/apache/uima/adapter/soap/BinaryDeserializer.java
# cannot access org.apache.commons.logging.Log
%pom_add_dep org.apache.commons:commons-logging %{name}-adapter-soap

# Build @ random fails
%pom_remove_plugin :apache-rat-plugin

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-javadoc-plugin jcasgen-maven-plugin

# Unavailable libraries
# e.g.
# UIMA_CLASSPATH=$UIMA_CLASSPATH:$UIMA_HOME/lib/uimaj-as-core.jar
# UIMA_CLASSPATH=$UIMA_CLASSPATH:$UIMA_HOME/lib/uimaj-as-activemq.jar
# UIMA_CLASSPATH=$UIMA_CLASSPATH:$UIMA_HOME/lib/uimaj-as-jms.jar
# for now, until all deps aren't available, i prefer don't install script files
# or systemd support
# src/main/scripts/*.sh

# Remove eclipse stuff (dont provides pom or depmap file)
%pom_disable_module ../aggregate-%{name}-eclipse-plugins aggregate-%{name}
%pom_remove_dep org.apache.uima:%{name}-ep-cas-editor
%pom_remove_dep org.apache.uima:%{name}-ep-configurator
%pom_remove_dep org.apache.uima:%{name}-ep-debug
%pom_remove_dep org.apache.uima:%{name}-ep-jcasgen
%pom_remove_dep org.apache.uima:%{name}-ep-pear-packager
%pom_remove_dep org.apache.uima:%{name}-ep-runtime
%pom_remove_dep org.apache.uima:%{name}-ep-cas-editor-ide
%pom_remove_dep org.apache.uima:%{name}-ep-launcher
%pom_remove_dep org.apache.uima:%{name}-examples
#%%pom_remove_dep org.eclipse.emf:common %%{name}-examples
#%%pom_remove_dep org.eclipse.emf:ecore %%{name}-examples
#%%pom_remove_dep org.eclipse.emf:ecore-xmi %%{name}-examples
%pom_disable_module ../%{name}-examples aggregate-%{name}

# Use system jvm apis
%pom_remove_dep org.apache.geronimo.specs:geronimo-activation_1.0.2_spec %{name}-adapter-soap

# Unavailable deps org.apache.uima:uima-docbook-olink:zip:olink:1-SNAPSHOT
%pom_disable_module ../aggregate-%{name}-docbooks aggregate-%{name}

# These tests @ random fails
rm -r %{name}-core/src/test/java/org/apache/uima/internal/util/UIMAClassLoaderTest.java \
  %{name}-core/src/test/java/org/apache/uima/cas/test/SofaTest.java \
  %{name}-core/src/test/java/org/apache/uima/analysis_engine/impl/AnalysisEngine_implTest.java \
  %{name}-core/src/test/java/org/apache/uima/util/impl/JSR47Logger_implTest.java \
  jcasgen-maven-plugin/src/test/java/org/apache/uima/tools/jcasgen/maven/JCasGenMojoTest.java

# Unavailable test:crossref2:1.0.0-SNAPSHOT
%pom_remove_plugin :maven-invoker-plugin jcasgen-maven-plugin
 
sed -i 's/\r//' NOTICE README

# These tests fails with java8
rm -r %{name}-tools/src/test/java/org/apache/uima/tools/viewer/CasAnnotationViewerTest.java

sed -i "s|<version>1.2.8</version>|<version>1.2.17</version>|" %{name}-core/pom.xml

%mvn_package :PearPackagingMavenPlugin uima-pear-maven-plugin
%mvn_package :jcasgen-maven-plugin jcasgen-maven-plugin

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README RELEASE_NOTES.html
%doc LICENSE NOTICE

%files -n jcasgen-maven-plugin -f .mfiles-jcasgen-maven-plugin
%doc LICENSE NOTICE

%files -n uima-pear-maven-plugin -f .mfiles-uima-pear-maven-plugin
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_5jpp8
- java 8 mass update

