Epoch: 0
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          stax-ex
Version:       1.7.1
Release:       alt1_6jpp7
Summary:       StAX API extensions
License:       CDDL or GPLv2
Url:           https://stax-ex.dev.java.net
# svn export https://svn.java.net/svn/stax-ex~svn/tags/stax-ex-1.7.1 stax-ex-1.7.1
# find stax-ex-1.7.1/ -name '*.jar' -delete
# tar czf stax-ex-1.7.1.tar.gz stax-ex-1.7.1
Source0:       %{name}-%{version}.tar.gz

BuildRequires: bea-stax
BuildRequires: dos2unix
BuildRequires: junit
BuildRequires: jvnet-parent
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildArch:     noarch
Source44: import.info

%description
This project develops a few extensions to complement JSR-173 StAX API in the
following area.

* Enable parser instance reuse (which is important in the
  high-performance environment like JAXB and JAX-WS)
* Improve the support for reading from non-text XML infoset,
  such as FastInfoset.
* Improve the namespace support.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%pom_remove_dep javax.activation:activation

# Convert the license to UTF-8:
mv LICENSE.txt LICENSE.txt.tmp
iconv -f ISO-8859-1 -t UTF-8 LICENSE.txt.tmp > LICENSE.txt
dos2unix LICENSE.txt

%build

%mvn_file :stax-ex %{name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_4jpp7
- new release

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_2jpp7
- fc update

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_2jpp7
- new release

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_7jpp6
- added repolib

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp5
- fixed docdir ownership

* Wed Oct 01 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp5
- converted from JPackage by jppimport script

