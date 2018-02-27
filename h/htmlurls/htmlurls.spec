Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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

Name:           htmlurls
Version:        1.0.004
Release:        alt2_1jpp6
Summary:        Static Url manipulation utilities

Group:          Development/Java
License:        LGPL
URL:            http://htmlurls.sourceforge.net

Source0:        htmlurls_1_0_004.zip
Source1:        htmlurls-build.xml
Source2:        htmlurls-1.0.004.pom

BuildRequires: ant >= 1.6.5
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: jpackage-utils >= 0:5.0.0

Requires: jpackage-utils >= 0:5.0.0

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
HTMLURLs is an Open Source Java class that contains a 
collection of static utility methods to manipulate and 
convert URL (Uniform Resource Locator) addresses from 
java.lang.String to java.net.URL objects and vice versa.
The HTMLURLs class is very useful in Web-based application 
development because speeds up the URLs manipulation, that 
is a common task.
The HTMLURLs main features are:
* allows set up a java.net.URL object starting from various
  String representation;
* checks if an URL is absolute or relative to the current 
  local path;
* get full canonical URL address by resolving various 
  combined relative paths 
  (e.g.: "http://www.site.com/dir/subdir/../image.gif" 
  became "http://www.site.com/dir/image.gif"); this 
  last case resolve a very common problem in 
  Web-applications.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
cp %{SOURCE1} build.xml

%build
export OPT_JAR_LIST="ant/ant-junit junit"
%ant -Djunit.jar=$(build-classpath junit) jar test javadoc

%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}
%__install -m 644 build/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

%__install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
%__install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap com.tecnick.htmlutils %{name} %{version} JPP %{name}

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a build/javadoc %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%doc *.TXT
%{_javadir}/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.004-alt2_1jpp6
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.004-alt1_1jpp6
- new version

