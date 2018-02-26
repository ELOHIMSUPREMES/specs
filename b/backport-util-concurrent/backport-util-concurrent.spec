Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

Name:		backport-util-concurrent
Summary:	Backport of java.util.concurrent API, introduced in Java 5.0
Version:	3.1
Release:	alt1_8jpp7
URL:		http://backport-jsr166.sourceforge.net
License:	Public Domain
Group:		Development/Java
Source0:        http://downloads.sourceforge.net/backport-jsr166/%{name}-%{version}-src.tar.gz
Source1:	http://repo1.maven.org/maven2/backport-util-concurrent/backport-util-concurrent/3.1/backport-util-concurrent-3.1.pom

BuildRequires:	jpackage-utils >= 0:1.7.2
BuildRequires:	ant >= 0:1.6.5
BuildRequires:	junit
BuildArch:	noarch
Requires:	jpackage-utils
Requires(post):		jpackage-utils >= 0:1.7.2
Requires(postun):	jpackage-utils >= 0:1.7.2
Source44: import.info


%description
This package is the backport of java.util.concurrent API, introduced in
Java 5.0, to Java 1.4. The backport is based on public-domain sources
from the JSR 166 CVS repository, and the dl.util.concurrent package.

%package javadoc
Group:			Development/Java
Summary:		Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}-src

find . -name '*.?ar' | xargs rm -f

build-jar-repository -s -p external \
		junit

%build
unset CLASSPATH
ant dist test

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 backport-util-concurrent-dist/%{name}.jar \
		$RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
		$RPM_BUILD_ROOT%{_javadir}/%{name}.jar


# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr backport-util-concurrent-dist/doc/api/* \
		$RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc license.html
%doc README.html
%{_javadir}/*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}

%files javadoc
%doc license.html
%{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_8jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_4jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_3jpp5
- new version

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

