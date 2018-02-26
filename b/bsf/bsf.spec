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

Name:           bsf
Version:        2.4.0
Release:        alt3_13jpp7
Epoch:          1
Summary:        Bean Scripting Framework
License:        ASL 2.0
URL:            http://commons.apache.org/bsf/
Group:          Development/Java
Source0:        http://apache.osuosl.org/jakarta/%{name}/source/%{name}-src-%{version}.tar.gz
Source1:        %{name}-pom.xml
Patch0:         build-file.patch
Patch1:	        build.properties.patch
BuildRequires:  jpackage-utils >= 1.6
BuildRequires:  ant
BuildRequires:  xalan-j2
BuildRequires:  jython
BuildRequires:  rhino
BuildRequires:  apache-commons-logging
Requires:       xalan-j2
Requires:       apache-commons-logging
Requires:       jpackage-utils
BuildArch:      noarch
Source44: import.info
%add_findreq_skiplist /usr/share/bsf-*

%description
Bean Scripting Framework (BSF) is a set of Java classes which provides
scripting language support within Java applications, and access to Java
objects and methods from scripting languages. BSF allows one to write
JSPs in languages other than Java while providing access to the Java
class library. In addition, BSF permits any Java application to be
implemented in part (or dynamically extended) by a language that is
embedded within it. This is achieved by providing an API that permits
calling scripting language engines from within Java, as well as an
object registry that exposes Java objects to these scripting language
engines.

BSF supports several scripting languages currently:
* Javascript (using Rhino ECMAScript, from the Mozilla project)
* Python (using either Jython or JPython)
* Tcl (using Jacl)
* NetRexx (an extension of the IBM REXX scripting language in Java)
* XSLT Stylesheets (as a component of Apache XML project's Xalan and
Xerces)

In addition, the following languages are supported with their own BSF
engines:
* Java (using BeanShell, from the BeanShell project)
* JRuby
* JudoScript

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
# remove all binary libs
find . -name "*.jar" -exec %{__rm} -f {} \;
%{__rm} -fr bsf

%patch0 -p1
%patch1 -p1

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
export CLASSPATH=$(build-classpath apache-commons-logging jython xalan-j2 rhino)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar
%{__rm} -rf bsf/src/org/apache/bsf/engines/java
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  javadocs

%install
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 build/lib/%{name}.jar \
             %{buildroot}%{_javadir}/%{name}.jar
# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}
%{__cp} -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}

%{__install} -DTm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.bsf:%{name}"

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE.txt AUTHORS.txt CHANGES.txt NOTICE.txt README.txt TODO.txt RELEASE-NOTE.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_13jpp7
- fc version

* Tue Jan 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_11jpp6
- restored repolib

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt2_11jpp6
- new jpp relase

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt2_2jpp6
- fixed repolib

* Fri Jan 07 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt1_2jpp6
- new version

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 1:2.3.0-alt1_13jpp5
- downgrade to match 5.0; added repolib

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt4_1jpp1.7
branch 4.0 compatible build

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt3_1jpp1.7
- do disabled python findreq on jython code
- added commons-lang dependency

* Tue Nov 27 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt2_1jpp1.7
- disabled python findreq on jython code

* Sun Nov 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_1jpp1.7
- updated to new jpackage release

* Mon Oct 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt2_11jpp1.7
- resurrected from orphaned
- added obsolete jakarta-bsf

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_11jpp1.7
- converted from JPackage by jppimport script

