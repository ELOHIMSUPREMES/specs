Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:          apache-commons-pool2
Version:       2.4.1
Release:       alt1_1jpp8
Summary:       Apache Commons Object Pooling Library 2.x series
License:       ASL 2.0
URL:           http://commons.apache.org/proper/commons-pool/
Source0:       http://www.apache.org/dist/commons/pool/source/commons-pool2-%{version}-src.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(junit:junit)
%if %{fedora} > 20
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
%else
BuildRequires: mvn(org.apache.commons:commons-parent)
%endif
BuildRequires: mvn(org.ow2.asm:asm-util)

BuildArch:     noarch
Source44: import.info

%description
The Apache Commons Pool open source software library provides an
object pooling API and a number of object pool implementations.
Version 2 of Apache Commons Pool contains a completely re-written
pooling implementation compared to the 1.x series. In addition
to performance and scalability improvements, version 2 includes
robust instance tracking and pool monitoring.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n commons-pool2-%{version}-src

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

%mvn_file : %{name} commons-pool2

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_1jpp8
- new version

