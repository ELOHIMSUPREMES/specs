Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           apache-commons-csv
Version:        1.1
Release:        alt1_2jpp8
Summary:        Utilities to assist with handling of CSV files
License:        ASL 2.0
URL:            https://commons.apache.org/proper/commons-csv/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/csv/source/commons-csv-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.h2database:h2)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
Source44: import.info

%description
Commons CSV was started to unify a common and simple interface for
reading and writing CSV files under an ASL license.

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n commons-csv-%{version}-src
sed -i 's/\r//' *.txt
find -name profile.jacoco -delete

# Unwanted plugins
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file ":{*}" %{name} @1
%mvn_alias : commons-csv:

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.7.svn1071189jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.6.svn1071189jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.3.svn1071189jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.3.svn1071189jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.svn1071189jpp7
- new version

