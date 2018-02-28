Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
%global master_version 4
Name:          struts
Version:       1.3.10
Release:       alt4_15jpp8
Summary:       Web application framework
License:       ASL 2.0
URL:           http://struts.apache.org/
# wget http://www.apache.org/dist/struts/source/struts-1.3.10-src.zip
# remove non free resources
# unzip -qq struts-1.3.10-src.zip
# rm -r struts-1.3.10/src/core/src/main/resources/org/apache/struts/resources/web-app_2_3.dtd
# tar czf struts-1.3.10-clean-src.tar.gz struts-1.3.10
Source0:       %{name}-%{version}-clean-src.tar.gz
# wget -O struts-master-4-pom.xml http://svn.apache.org/repos/asf/struts/maven/tags/STRUTS_MASTER_4/pom.xml
Source1:       %{name}-master-%{master_version}-pom.xml
# add struts-master relativePath
Patch0:        %{name}-%{version}-parent-pom.patch
# add 
#  org.jboss.spec.javax.el
#  org.apache.maven.plugins maven-resources-plugin configuration
# change 
#  myfaces myfaces-jsf-api 1.0.9 with org.jboss.spec.javax.faces
#  jakarta-taglibs-standard with taglibs-standard-jstlel
#  javax.servlet servlet-api with org.jboss.spec.javax.servlet
#  javax.servlet jsp-api with org.jboss.spec.javax.servlet.jsp
# fix
#  bsf gId
#  maven-compiler-plugin build source/target
#  build for junit servlet-3.1-api
Patch1:        %{name}-%{version}-jboss.patch
# Thanks to Arun Babu Neelicattu aneelica@redhat.com
# and Brandon.Vincent@asu.edu
Patch2:        struts-1.3.10-CVE-2014-0114.patch

Patch3:        struts-1.3.10-CVE-2015-0899.patch

BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(commons-chain:commons-chain)
BuildRequires: mvn(commons-digester:commons-digester)
BuildRequires: mvn(commons-fileupload:commons-fileupload)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(commons-validator:commons-validator)
BuildRequires: mvn(junit:junit)
%if %{?fedora} >= 21
BuildRequires: mvn(log4j:log4j:1.2.17)
%else
BuildRequires: mvn(log4j:log4j)
%endif
BuildRequires: mvn(org.apache.bsf:bsf)
BuildRequires: mvn(org.apache.taglibs:taglibs-standard-jstlel)
BuildRequires: mvn(org.jboss.spec.javax.el:jboss-el-api_3.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.faces:jboss-jsf-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.3_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires: mvn(oro:oro)

BuildRequires: maven-local

BuildArch:     noarch
Obsoletes:     %{name}-manual < %{version}
Obsoletes:     %{name}-webapps-tomcat5 < %{version}
Source44: import.info

%description
Welcome to the Struts Framework! The goal of this project is to provide
an open source framework useful in building web applications with Java
Servlet and JavaServer Pages (JSP) technology. Struts encourages
application architectures based on the Model-View-Controller (MVC)
design paradigm, colloquially known as Model 2 in discussions on various
servlet and JSP related mailing lists.
Struts includes the following primary areas of functionality:
A controller servlet that dispatches requests to appropriate Action
classes provided by the application developer.
JSP custom tag libraries, and associated support in the controller
servlet, that assists developers in creating interactive form-based
applications.
Utility classes to support XML parsing, automatic population of
JavaBeans properties based on the Java reflection APIs, and
internationalization of prompts and messages.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find -name "*.jar" -delete
find -name "*.class" -delete
%patch0 -p0
%patch1 -p1
%patch2 -p0
%patch3 -p1

sed -i 's/\r//' LICENSE.txt NOTICE.txt

# fix non ASCII chars
for s in src/tiles/src/main/java/org/apache/struts/tiles/ComponentDefinition.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%pom_remove_parent src
#cp -p %%{SOURCE1} pom.xml

cd src
%mvn_file :%{name}-core %{name}/core
%mvn_file :%{name}-el %{name}/el
%mvn_file :%{name}-extras %{name}/extras
%mvn_file :%{name}-faces %{name}/faces
%mvn_file :%{name}-mailreader-dao %{name}/mailreader-dao
%mvn_file :%{name}-scripting %{name}/scripting
%mvn_file :%{name}-taglib %{name}/taglib
%mvn_file :%{name}-tiles %{name}/tiles

%build

cd src
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install

(
cd src
%mvn_install
)
rm -rf $RPM_BUILD_ROOT/var/lib/tomcat?/webapps/struts-documentation/download.cgi

%files -f src/.mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files javadoc -f src/.mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt4_15jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt4_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt4_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt4_5jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt3_5jpp7
- fc version

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt3_2jpp6
- fixed build using htmlunit1

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt2_2jpp6
- fixed build with java 7

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt1_2jpp6
- new version

* Fri Mar 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.8-alt2_2jpp5
- build with checkstyle4

* Sun Mar 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3.8-alt1_2jpp5
- fixed repocop warnings

* Fri Mar 14 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt4_5jpp1.7
- disabled struts-tomcat4

* Wed Sep 12 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt3_5jpp1.7
- rebuild to remove duplicate struts

* Sat Aug 11 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt2_5jpp1.7
- converted from JPackage by jppimport script

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt1_5jpp1.7
- new version

* Thu Apr 19 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.2.6-alt4
- Built with explicit java-1.5.0

* Wed Mar 22 2006 Vladimir Lettiev <crux@altlinux.ru> 1.2.6-alt3
- Fix build with j2se-1.5

* Wed Apr 06 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.6-alt2
- packaged webapps for tomcats

* Tue Apr 05 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Tue Apr 05 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt1
- Initial build for ALT Linux Sisyphus

