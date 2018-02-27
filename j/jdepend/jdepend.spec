# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           jdepend
Version:        2.9.1
Release:        alt3_7jpp7
Epoch:          0
Summary:        Java Design Quality Metrics
License:        BSD
URL:            http://www.clarkware.com/
Group:          Development/Java
#Downloaded from http://github.com/clarkware/jdepend/tarball/2.9.1
Source0:        clarkware-jdepend-5798059.tar.gz
Source1:        %{name}-%{version}.pom
BuildArch:      noarch

Requires:      jpackage-utils

BuildRequires: ant
BuildRequires: jpackage-utils
Source44: import.info

%description
JDepend traverses a set of Java class and source file directories and
generates design quality metrics for each Java package. JDepend allows
you to automatically measure the quality of a design in terms of its
extensibility, reusability, and maintainability to effectively manage
and control package dependencies.

%package javadoc
Summary:    Javadoc for %{name}
Group:      Development/Java
Requires:   %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:    Demos for %{name}
Group:      Development/Java
Requires:   %{name} = %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n clarkware-jdepend-5798059
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
# fix strange permissions
find . -type d -exec chmod 755 {} \;

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} 
rm -rf build/docs/api
# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr sample $RPM_BUILD_ROOT%{_datadir}/%{name}
# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
# depmap
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc README LICENSE docs
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_7jpp7
- fc update

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_3jpp6
- added pom

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_1jpp5
- new jpackage release

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_1jpp1.7
- rebuild with new packages

* Wed Apr 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt2_1jpp1.7
- converted from JPackage by jppimport script

* Wed Apr 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Mon Sep 20 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.2-alt1
- Updated to upstream release 2.8.2
- Disabled debug compiler option by default

* Mon Jun 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.7-alt1
- New upstream release

* Fri Oct 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6-alt1
- Ported to Sisyphus from JPackage
