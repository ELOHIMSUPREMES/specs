Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

%global parent plexus
%global subname utils

Name:           plexus-utils
Version:        3.0.14
Release:        alt1_1jpp7
Summary:        Plexus Common Utilities
# ASL 1.1: several files in src/main/java/org/codehaus/plexus/util/ 
# xpp: src/main/java/org/codehaus/plexus/util/xml/pull directory
# ASL 2.0 and BSD:
#      src/main/java/org/codehaus/plexus/util/cli/StreamConsumer
#      src/main/java/org/codehaus/plexus/util/cli/StreamPumper
#      src/main/java/org/codehaus/plexus/util/cli/Commandline            
# Public domain: src/main/java/org/codehaus/plexus/util/TypeFormat.java
# rest is ASL 2.0
License:        ASL 1.1 and ASL 2.0 and xpp and BSD and Public Domain
Group:          Development/Java
URL:            http://plexus.codehaus.org/
Source0:        https://github.com/sonatype/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.6
Requires:       jpackage-utils

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Source44: import.info

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} .

# Generate OSGI info
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_xpath_inject "pom:build/pom:plugins" "
        <plugin>
          <groupId>org.apache.felix</groupId>
          <artifactId>maven-bundle-plugin</artifactId>
          <extensions>true</extensions>
          <configuration>
            <instructions>
              <_nouses>true</_nouses>
              <Export-Package>org.codehaus.plexus.util.*;org.codehaus.plexus.util.cli.*;org.codehaus.plexus.util.cli.shell.*;org.codehaus.plexus.util.dag.*;org.codehaus.plexus.util.introspection.*;org.codehaus.plexus.util.io.*;org.codehaus.plexus.util.reflection.*;org.codehaus.plexus.util.xml.*;org.codehaus.plexus.util.xml.pull.*</Export-Package>
            </instructions>
          </configuration>
        </plugin>"

%build
mvn-rpmbuild install javadoc:javadoc -Dmaven.test.failure.ignore=true

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{parent}
install -pm 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/plexus/utils.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-%{subname}.pom

%add_maven_depmap -a "plexus:plexus-utils" JPP.%{name}.pom plexus/utils.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files -f .mfiles
%doc NOTICE.txt LICENSE-2.0.txt

%files javadoc
%doc NOTICE.txt LICENSE-2.0.txt
%doc %{_javadocdir}/%{name}

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.14-alt1_1jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.9-alt1_5jpp7
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_3jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_2jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

