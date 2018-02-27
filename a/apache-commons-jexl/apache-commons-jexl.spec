Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global jarname commons-jexl

Name:           apache-%{jarname}
Version:        2.1.1
Release:        alt2_8jpp7
Summary:        Java Expression Language (JEXL)

Group:          Development/Java
License:        ASL 2.0
URL:            http://commons.apache.org/jexl
Source0:        http://www.apache.org/dist/commons/jexl/source/%{jarname}-%{version}-src.tar.gz
# Patch to fix test failure with junit 4.11
Patch0:         001-Fix-tests.patch

BuildRequires:  maven-local
BuildRequires:  javacc-maven-plugin

BuildArch:      noarch

Provides:       %{jarname} = %{version}-%{release}
Source44: import.info

%description
Java Expression Language (JEXL) is an expression language engine which can be
embedded in applications and frameworks.  JEXL is inspired by Jakarta Velocity
and the Expression Language defined in the JavaServer Pages Standard Tag
Library version 1.1 (JSTL) and JavaServer Pages version 2.0 (JSP).  While
inspired by JSTL EL, it must be noted that JEXL is not a compatible
implementation of EL as defined in JSTL 1.1 (JSR-052) or JSP 2.0 (JSR-152).
For a compatible implementation of these specifications, see the Commons EL
project.

JEXL attempts to bring some of the lessons learned by the Velocity community
about expression languages in templating to a wider audience.  Commons Jelly
needed Velocity-ish method access, it just had to have it.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Provides:       %{jarname}-javadoc = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{jarname}-%{version}-src
%patch0 -p1 -b .test
# Java 1.6 contains bsf 3.0, so we don't need the dependency in the pom.xml file
%pom_remove_dep org.apache.bsf:bsf-api
find \( -name '*.jar' -o -name '*.class' \) -delete
# Fix line endings
find -name '*.txt' -exec sed -i 's/\r//' '{}' +


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}


%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_3jpp7
- new version

* Tue Feb 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_5jpp6
- fixed obsoletes (closes: #25046)

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_5jpp6
- new version

