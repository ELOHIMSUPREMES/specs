BuildRequires: /proc
BuildRequires: jpackage-compat
%global artifactId plexus-component-factories

Name:		plexus-component-factories-pom
Version:	1.0
Release:	alt1_0.6.alpha11jpp7
Summary:	Plexus Component Factories POM
BuildArch:	noarch
Group:		Development/Java
License:	ASL 2.0
URL:		http://plexus.codehaus.org/
Source0:	http://repo1.maven.org/maven2/org/codehaus/plexus/%{artifactId}/%{version}-alpha-11/%{artifactId}-%{version}-alpha-11.pom
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:	maven-local
Source44: import.info


%description
This package provides Plexus Component Factories parent POM used by different
Plexus packages.

%prep
%setup -cT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_xpath_remove pom:modules

%build
%mvn_alias : plexus:
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.6.alpha11jpp7
- new version

