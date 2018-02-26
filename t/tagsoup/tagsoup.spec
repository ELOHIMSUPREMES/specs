# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: xalan-j2
Requires: xalan-j2
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
#    distributio4.3n.
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

Name:           tagsoup
Version:        1.2.1
Release:        alt1_2jpp7
Epoch:          0
Summary:        A SAX-compliant HTML parser written in Java 
License:        GPLv2+ or AFL
Source0:        http://home.ccil.org/~cowan/XML/tagsoup/tagsoup-1.2.1-src.zip
URL:            http://home.ccil.org/~cowan/XML/tagsoup/
Group:          Development/Java
Source1:        http://repo1.maven.org/maven2/org/ccil/cowan/tagsoup/tagsoup/%{version}/tagsoup-%{version}.pom
# fix version
Patch0:         tagsoup-1.2.1-man.patch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant
BuildRequires:  ant-apache-xalan2
BuildRequires:  bash
BuildRequires:  xalan-j2
Requires:       jpackage-utils >= 0:1.6
# see https://bugzilla.redhat.com/show_bug.cgi?id=502328
ExcludeArch:    ppc64
BuildArch:      noarch
Source44: import.info

%description
TagSoup is a SAX-compliant parser written in Java that, instead of
parsing well-formed or valid XML, parses HTML as it is found in the wild: nasty
and brutish, though quite often far from short. TagSoup is designed for people
who have to process this stuff using some semblance of a rational application
design. By providing a SAX interface, it allows standard XML tools to be
applied to even the worst HTML.

%package javadoc
Summary:       Javadoc for %{name}
Group:         Development/Java
Requires:      jpackage-utils >= 0:1.6
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

find . -name '*.class' -delete
find . -name "*.jar" -delete
%patch0 -p0

%build

export CLASSPATH=$(build-classpath xalan-j2-serializer xalan-j2)
ant \
  -Dtagsoup.version=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  dist docs-api

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 dist/lib/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/

%files
%{_javadir}/%{name}.jar
%{_mandir}/man1/%{name}.1*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc CHANGES LICENSE README TODO %{name}.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_2jpp7
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_3jpp5
- rebuild with default profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_3jpp5
- jpp5 build

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

