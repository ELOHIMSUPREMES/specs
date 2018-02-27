Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-reporting-api
Version:        3.0
Release:        alt1_0jpp7
# Maven-shared defines maven-reporting-api version as 3.0
Epoch:          1
Summary:        API to manage report generation
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-reporting-api
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-reporting-api-3.0 maven-reporting-api-3.0
# tar caf maven-reporting-api-3.0.tar.xz maven-reporting-api-3.0/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)

#Obsoletes:      maven-shared-reporting-api < %{epoch}:%{version}-%{release}
Provides:       maven-shared-reporting-api = %{epoch}:%{version}-%{release}
Source44: import.info

%description
API to manage report generation. Maven-reporting-api is included in Maven 2.x
core distribution, but moved to shared components to achieve report decoupling
from Maven 3 core.

This is a replacement package for maven-shared-reporting-api

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q
cp %{SOURCE1} LICENSE.txt

%build
# Previous package provides groupIds org.apache.maven.shared and org.apache.maven.reporting
%mvn_alias : org.apache.maven.shared:maven-reporting-api
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt1_0jpp7
- new version

