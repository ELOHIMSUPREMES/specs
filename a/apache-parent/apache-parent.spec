BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           apache-parent
Version:        10
Release:        alt2_13jpp7
Summary:        Parent pom file for Apache projects
Group:          Development/Java
License:        ASL 2.0
URL:            http://apache.org/
Source0:        http://svn.apache.org/repos/asf/maven/pom/tags/apache-10/pom.xml
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  jpackage-utils
BuildRequires:  apache-resource-bundles
BuildRequires:  maven-remote-resources-plugin

Requires:       apache-resource-bundles
Source44: import.info

%description
This package contains the parent pom file for apache projects.


%prep
%setup -n %{name}-%{version} -Tc

# This simplifies work with child projects that can use generics
cp %{SOURCE0} .
sed -i 's:<source>1.4</source>:<source>1.5</source>:' pom.xml
sed -i 's:<target>1.4</target>:<target>1.5</target>:' pom.xml

cp %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_10jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_7jpp7
- rebuild with new apache-resource-bundles

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 10-alt1_7jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 10-alt1_5jpp7
- new release

