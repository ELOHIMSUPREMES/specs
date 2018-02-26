Requires: xmldb-api-sdk
BuildRequires: xmldb-api-sdk
BuildRequires: docbook-xml docbook-dtds
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

%global base_name jaxme

Name:           ws-jaxme
Version:        0.5.2
Release:        alt2_6jpp7
Epoch:          0
Summary:        Open source implementation of JAXB

Group:          Development/Java
License:        ASL 2.0
URL:            http://ws.apache.org/jaxme/
# svn export http://svn.apache.org/repos/asf/webservices/archive/jaxme/tags/R0_5_2/ ws-jaxme-0.5.2
# tar czf ws-jaxme-0.5.2-src.tar.gz ws-jaxme-0.5.2
Source0:        ws-jaxme-0.5.2-src.tar.gz
Source1:        ws-jaxme-bind-MANIFEST.MF
# generated docs with forrest-0.5.1
Patch0:         ws-jaxme-docs_xml.patch
Patch1:         ws-jaxme-catalog.patch
Patch2:         ws-jaxme-system-dtd.patch
Patch3:         ws-jaxme-jdk16.patch
Patch4:         ws-jaxme-ant-scripts.patch
Patch5:         ws-jaxme-use-commons-codec.patch
# Remove xmldb-api, deprecated since f17
Patch6:         ws-jaxme-remove-xmldb.patch
Patch7:         ws-jaxme-0.5.2-class-version15.patch
BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-apache-resolver
BuildRequires:  antlr
BuildRequires:  apache-commons-codec
BuildRequires:  junit
BuildRequires:  hsqldb
BuildRequires:  log4j
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:	docbook-style-xsl
BuildRequires:  docbook-dtds
BuildRequires:  zip
Requires:       antlr
Requires:       apache-commons-codec
Requires:       junit
Requires:       hsqldb
Requires:       log4j
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       jpackage-utils
Source44: import.info

%description
A Java/XML binding compiler takes as input a schema 
description (in most cases an XML schema, but it may 
be a DTD, a RelaxNG schema, a Java class inspected 
via reflection, or a database schema). The output is 
a set of Java classes:
* A Java bean class matching the schema description. 
  (If the schema was obtained via Java reflection, 
  the original Java bean class.)
* Read a conforming XML document and convert it into 
  the equivalent Java bean.
* Vice versa, marshal the Java bean back into the 
  original XML document.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Requires(postun): jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Java
BuildArch: noarch

%description    manual
%{summary}.

%prep
%setup -q
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%patch0 -p0
%patch1 -p0
%patch2 -p1
DOCBOOKX_DTD=`%{_bindir}/xmlcatalog %{_datadir}/sgml/docbook/xmlcatalog "-//OASIS//DTD DocBook XML V4.5//EN" 2>/dev/null`
%{__perl} -pi -e 's|@DOCBOOKX_DTD@|$DOCBOOKX_DTD|' src/documentation/manual/jaxme2.xml
%patch3 -p1
%patch4 -b .sav
%patch5 -b .sav
%patch6 -p1
%patch7 -p1

%build
export CLASSPATH=$(build-classpath antlr hsqldb commons-codec junit log4j xerces-j2 xalan-j2)
ant all Docs.all \
-Dbuild.sysclasspath=first \
-Ddocbook.home=%{_datadir}/sgml/docbook \
-Ddocbookxsl.home=%{_datadir}/sgml/docbook/xsl-stylesheets

mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u dist/jaxmeapi-%{version}.jar META-INF/MANIFEST.MF

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{base_name}
for jar in dist/*.jar; do
   install -m 644 ${jar} $RPM_BUILD_ROOT%{_javadir}/%{base_name}/
done
(cd $RPM_BUILD_ROOT%{_javadir}/%{base_name} && 
    for jar in *-%{version}*; 
        do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; 
    done
)

(cd $RPM_BUILD_ROOT%{_javadir}/%{base_name} && 
    for jar in *.jar; 
        do ln -sf ${jar} ws-${jar}; 
    done
)

#javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/docs/src/documentation/content/apidocs \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf build/docs/src/documentation/content/apidocs

#manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr build/docs/src/documentation/content/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -pm 644 LICENSE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%doc LICENSE NOTICE
%{_javadir}/%{base_name}

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{name}

%files manual
%doc LICENSE NOTICE
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt2_6jpp7
- fc release

* Fri May 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt2_1jpp5
- explicitly selected java5 compiler

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt1_1jpp5
- added OSGi provides

* Tue Oct 23 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Sun May 06 2007 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2
- added JPackage compatible symlinks

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 0.3.1-alt1
- Initial build for ALT Linux Sisyphus

