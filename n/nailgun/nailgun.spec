# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define debug_package %{nil}

Name:     nailgun
Version:  0.7.1
Release:  alt1_9jpp7
Summary:  Framework for running Java from the cli without the JVM startup overhead
Group:    Development/Java
License:  ASL 2.0
URL:      http://martiansoftware.com/nailgun/
Source0:  http://downloads.sourceforge.net/project/nailgun/nailgun/0.7.1/nailgun-src-0.7.1.zip
Patch0:   remove-tools-jar-dependencies.patch

BuildRequires:  jpackage-utils
BuildRequires: ant
BuildRequires: ant-junit
Requires:  jpackage-utils
Source44: import.info

%description
Nailgun is a client, protocol, and server for running Java programs from the 
command line without incurring the JVM startup overhead. Programs run in the 
server (which is implemented in Java), and are triggered by the client 
(written in C), which handles all I/O.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
ant

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}

cp dist/nailgun-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

cp ng $RPM_BUILD_ROOT%{_bindir}/ng

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/nailgun.jar
%{_bindir}/ng
%doc LICENSE.txt README.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_7jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_6jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_5jpp7
- new version

