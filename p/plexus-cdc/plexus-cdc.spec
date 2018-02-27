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

%global parent plexus

%global subname cdc

Name:           %{parent}-%{subname}
Version:        1.0
Release:        alt11_0.19.a14jpp7
Epoch:          0
Summary:        Plexus Component Descriptor Creator
# Almost whole gleaner subpackage is ASL 2.0
License:        MIT and ASL 2.0
Group:          Development/Java
URL:            http://plexus.codehaus.org/
# svn export -r 7728 http://svn.codehaus.org/plexus/archive/plexus-tools/tags/plexus-tools-1.0.11/plexus-cdc plexus-cdc
# tar czf plexus-cdc-1.0-alpha-14.tar.gz plexus-cdc/
Source0:        %{name}-1.0-alpha-14.tar.gz
Source1:        %{name}-jpp-depmap.xml
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         %{name}-qdox-1.9.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  jdom
BuildRequires:  plexus-utils
BuildRequires:  maven-doxia-sitetools
BuildRequires:  qdox
Source44: import.info


%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}
cp -p %{SOURCE2} .

%patch0 -p1

%build
%mvn_file  : %{parent}/%{subname}
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt11_0.19.a14jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt11_0.18.a14jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt11_0.12.a14jpp7
- rebuild with maven-local

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt10_0.12.a14jpp7
- converted from JPackage by jppimport script

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.3.a10.8jpp6
- reverted to a10 for maven 2.0.8-28

* Thu Jan 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3.a11.3jpp6
- jpp 6 releases

* Thu Mar 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a11.2jpp5
- fixed unmet pom dependency on qdox

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a11.2jpp5
- new jpp release

* Wed Oct 01 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a10.1jpp5
- converted from JPackage by jppimport script

* Wed Oct 01 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a10.1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a4.3jpp1.7
- converted from JPackage by jppimport script

