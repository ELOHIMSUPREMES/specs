BuildRequires: maven-enforcer-plugin
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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

%define reltag GA
%define namedversion %{version}.%{reltag}

Name:           jboss-transaction-aspects
Version:        1.0.0
Release:        alt2_3jpp6
Epoch:          0
Summary:        JBoss Transaction Aspects
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn export http://anonsvn.jboss.org/repos/jbossas/projects/jboss-aspects/tags/jboss-transaction-aspects-1.0.0.GA/ jboss-transaction-aspects-1.0.0
Source0:        jboss-transaction-aspects-1.0.0.tar.gz
Source1:        jboss-transaction-aspects-jpp-depmap.xml
Source2:        jboss-transaction-aspects-settings.xml
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: jboss-aop2
Requires: jboss-aspects-common
Requires: jboss-common-core
Requires: jboss-common-logging-spi
Requires: jboss-integration
Requires: jta_1_1_api
BuildRequires: jboss-aspects-common
BuildRequires: jboss-parent >= 0:4
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-jboss-deploy-plugin
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: jboss-aop2
BuildRequires: jboss-common-core
BuildRequires: jboss-common-logging-spi
BuildRequires: jboss-integration
BuildRequires: jta_1_1_api
BuildArch:      noarch

%description
JBoss transaction aspects.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 

cp -p %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
%{_bindir}/mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 target/%{name}-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tests-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss.aspects %{name} %{namedversion} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-tests-%{version}.jar
%{_javadir}/%{name}-tests.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt2_3jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_3jpp6
- new version

