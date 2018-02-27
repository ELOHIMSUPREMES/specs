Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname oauth
Name:          java-oauth
Version:       20100601
Release:       alt2_7jpp7
Summary:       An open protocol to allow API authentication
License:       ASL 2.0
Url:           http://code.google.com/p/oauth/
# svn export http://oauth.googlecode.com/svn/code/java oauth-20100601
# find oauth-20100601 -name "*.bat" -delete
# find oauth-20100601 -name "*.class" -delete
# find oauth-20100601 -name "*.jar" -delete
# tar czf oauth-20100601-clean-src-svn.tar.gz oauth-20100601
Source0:       oauth-20100601-clean-src-svn.tar.gz

# remove unavailable test deps org.mortbay.jetty jetty-embedded 6.1.11
# unavailable deps disable this modules: core-old example test

# x test
# org.mortbay.jetty jetty-embedded 6.1.11

# x oauth-example-desktop
# org.codehaus.mojo appassembler-maven-plugin
# org.mortbay.jetty jetty-embedded 6.1.11

# x oauth-example-provider oauth-example-consumer
# org.mortbay.jetty jetty-maven-plugin

Patch0:        oauth-20100601-poms.patch

BuildRequires: httpcomponents-client
BuildRequires: jakarta-commons-httpclient
BuildRequires: tomcat-servlet-3.0-api

BuildRequires: maven-local
BuildRequires: maven-source-plugin

BuildArch:     noarch
Source44: import.info

%description
An open protocol to allow API authentication
in a simple and standard method from desktop and
web applications.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1

%build

%mvn_file :%{oname} %{oname}/%{oname}
%mvn_file :%{oname}-consumer %{oname}/%{oname}-consumer
%mvn_file :%{oname}-httpclient3 %{oname}/%{oname}-httpclient3
%mvn_file :%{oname}-httpclient4 %{oname}/%{oname}-httpclient4
%mvn_file :%{oname}-provider %{oname}/%{oname}-provider
# unavailable test deps
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 20100601-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 20100601-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 20100601-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 20100601-alt1_3jpp7
- new version

