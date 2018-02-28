%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global commit 41fddda1a4f430e45bef0154e1fdfe5671025f1e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          vecmath
Version:       1.6.0
Release:       alt1_0.5.20130710git41fdddajpp8
Summary:       The 3D vector math Java package, javax.vecmath
Group:         Development/Java
# License is GNU General Public License, version 2, with the Classpath Exception
License:       GPLv2 with exceptions
URL:           http://github.com/hharrison/vecmath
Source0:       https://github.com/hharrison/vecmath/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# missing pom file
# https://bugzilla.redhat.com/show_bug.cgi?id=1022506
Source1:       https://repo1.maven.org/maven2/javax/vecmath/vecmath/1.5.2/vecmath-1.5.2.pom
# Fix link to javadoc and javadoc errors
Patch0:        vecmath-javadoc.patch
BuildArch:     noarch

BuildRequires: ant
BuildRequires: java-javadoc
BuildRequires: javapackages-local

Source44: import.info

%description
The 3D vector math Java package, javax.vecmath.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -qn %{name}-%{commit}
%patch0 -p1
sed -e "s|<version>1.5.2</version>|<version>1.6.0</version>|" %{SOURCE1} > %{name}.pom
%mvn_file javax.vecmath:vecmath %{name}

%build
%ant

%install
%mvn_artifact %{name}.pom build/jars/%{name}.jar
%mvn_install -J build/javadoc

%files -f .mfiles
%doc docs/api-changes* COPYRIGHT.txt LICENSE.txt LICENSE-SPEC.html

%files javadoc -f .mfiles-javadoc
%doc COPYRIGHT.txt LICENSE.txt LICENSE-SPEC.html

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_0.5.20130710git41fdddajpp8
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_5.20090922cvsjpp7
- new version

