# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

Summary:        Web Services Description Language Toolkit for Java
Name:           wsdl4j
Version:        1.6.3
Release:        alt1_1jpp7
Epoch:          0
Group:          Development/Java
License:        CPL
URL:            http://sourceforge.net/projects/wsdl4j
BuildArch:      noarch
Source0:        http://downloads.sourceforge.net/project/wsdl4j/WSDL4J/%{version}/wsdl4j-src-%{version}.zip
Source1:        %{name}-MANIFEST.MF
Source2:        http://repo1.maven.org/maven2/wsdl4j/wsdl4j/%{version}/wsdl4j-%{version}.pom
Requires:       jpackage-utils
BuildRequires:  ant ant-junit
BuildRequires:  jpackage-utils
BuildRequires:  zip
Source44: import.info

%description
The Web Services Description Language for Java Toolkit (WSDL4J) allows the
creation, representation, and manipulation of WSDL documents describing
services.  This code base will eventually serve as a reference implementation
of the standard created by JSR110.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-1_6_3

%build
ant compile javadocs

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/%{name}.jar META-INF/MANIFEST.MF

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 644 build/lib/qname.jar $RPM_BUILD_ROOT%{_javadir}/qname.jar

# POMs
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

%files
%doc license.html
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc license.html
%{_javadocdir}/%{name}

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.3-alt1_1jpp7
- new version

* Fri Mar 22 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt4_7jpp7
- fc update

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt4_7jpp6
- jpp 6 release

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt4_5jpp6
- fixed OSGi provides

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt3_5jpp6
- added OSGi provides

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_6jpp5
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_4jpp5
- alternatives 0.4

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_3jpp5
- converted from JPackage by jppimport script

* Thu Dec 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_2jpp1.7
- removed ghost jar

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_2jpp1.7
- updated to new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_4jpp1.7
- converted from JPackage by jppimport script

* Thu Mar 24 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt1
- 1.5
- rpm-build-java macroces

* Fri Sep 24 2004 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt2
- corrected requires (xerces-j -> jaxp_parser_impl)

* Fri Sep 17 2004 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1
- Rebuild for ALT Linux Sisyphus
- spec cleanup

* Mon Aug 30 2004 Ralph Apel <r.apel at r-apel.de> 0:1.4-3jpp
- Build with ant-1.6.2

* Thu Jun 26 2003 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net> 0:1.4-2jpp
- Do not drop qname.jar

* Tue May 06 2003 David Walluck <david@anti-microsoft.org> 0:1.4-1jpp
- 1.4
- update for JPackage 1.5

* Sat Sep  7 2002 Ville Skytt� <ville.skytta at iki.fi> 1.1-1jpp
- First JPackage release.
