BuildRequires: /proc
BuildRequires: jpackage-compat
%define api_version 1.0
%define pkg_name geronimo-jaspic_%{api_version}_spec
Name:          geronimo-jaspic-spec
Version:       1.0
Release:       alt1_2jpp7
Summary:       Java Authentication SPI for Containers
License:       ASL 2.0
Group:         Development/Java
URL:           http://geronimo.apache.org/
Source0:       http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.tar.gz

Patch0:        geronimo-jaspic-spec-use-parent-pom.patch

BuildArch:     noarch

BuildRequires: maven
BuildRequires: maven-plugin-bundle
BuildRequires: geronimo-parent-poms
BuildRequires: jpackage-utils

Requires:      jpackage-utils
Source44: import.info

%description
Java Authentication Service Provider Interface for Containers (JSR-196) api.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.


%prep
%setup -q -n %{pkg_name}-%{version}

for d in LICENSE NOTICE ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done
%patch0 -p0

%build
mvn-rpmbuild install javadoc:aggregate

%install
mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{pkg_name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc LICENSE NOTICE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2jpp7
- full version

