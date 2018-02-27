# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%define _without_gcj 1
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           swing-layout
Version:        1.0.4
Release:        alt1_8jpp7
Summary:        Natural layout for Swing panels
Group:          Development/Java
License:        LGPLv2
URL:            https://swing-layout.dev.java.net/
# https://svn.java.net/svn/swing-layout~svn/trunk/
Source0:        %{name}-%{version}-src.zip
# from http://java.net/jira/secure/attachment/27303/pom.xml
Source1:        %{name}-pom.xml
# use javac target/source 1.5
Patch0:         %{name}-%{version}-project_properties.patch
Patch1:         %{name}-%{version}-fix-incorrect-fsf-address.patch

BuildRequires:  jpackage-utils >= 1.6
BuildRequires:  ant
BuildRequires:  dos2unix

BuildArch:      noarch
Source44: import.info

%description
Extensions to Swing to create professional cross platform layout.

%package javadoc
Summary:        Javadoc documentation for Swing Layout
Group:          Development/Java
BuildArch: noarch

%description javadoc
Documentation for Swing Layout code.


%prep
%setup -q
dos2unix releaseNotes.txt
%patch0 -p0
%patch1 -p0
sed -i 's/\r//' COPYING

cp -p %{SOURCE1} pom.xml
sed -i "s|<version>1.0.3</version>|<version>%{version}</version>|" pom.xml

%build

%{ant} jar javadoc dist

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc releaseNotes.txt COPYING

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_7jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_5jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_4jpp7
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3jpp6
- update to new release by jppimport

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6jpp6
- added pom

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4jpp6
- new build for netbeans

* Mon Dec 08 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2jpp5
- converted from JPackage by jppimport script

