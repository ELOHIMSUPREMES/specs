BuildRequires: /proc
BuildRequires: jpackage-compat
# SVN revision used
%global svnrel 1340

Name:		jide-oss
Version:	2.7.6
Release:	alt1_7.1340svnjpp7
Summary:	Swing component library built on top of Java/Swing
License:	GPLv2 with exceptions
Group:		Development/Java
URL:		https://jide-oss.dev.java.net/

#This is an svn snapshot, to get this tarball :
#then to checkout the project source repository : svn checkout https://jide-oss.dev.java.net/svn/jide-oss/branches/trunk_%{version} jide-oss --username guest
#create the tarball : tar -cjvf jide-oss-%{version}-%{svnrel}svn.tar.bz2 jide-oss

Source0:	%{name}-%{version}-%{svnrel}svn.tar.bz2

#Patch0: remove an unknown character
Patch0:		jide-oss-Eclipse3xJideTabbedPaneUI.java.patch
#Patch1: use a standard component instead of a vendor specific extension
Patch1:		jide-oss-AquaJidePopupMenuUI.java.patch
Patch2:		jide-oss-name-clash.patch

BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	dos2unix
BuildRequires:	unix2dos
BuildRequires:	ant

Requires:	jpackage-utils
Source44: import.info

%description
JIDE Common Layer is Swing component library built on top of Java/Swing.
It is also the foundation of other component products from JIDE.
This project has over 30 Swing components and over 100k lines of code.
It greatly enhanced the default component set provided by Swing and allow 
developers to focus on business logic layer instead of making components.

JIDE Common Layer was originally developed by JIDE Software developers
as a foundation in order to build other more advanced components.
In April of 2007, JIDE Software decided to open source this common layer
so that more and more developers can leverage them instead of wasting time
building them again.

%package javadoc
Summary:	User documentation for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}
BuildArch: noarch

%description javadoc
User documentation for %{name}.

%package doc
Summary:	User documentation for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}

%description doc
User documentation for %{name}.

%prep
%setup -q -n %{name}
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;
sed -i "s|\r||g" LICENSE.txt

%patch0 -p1 -b .unknown_character
%patch1 -p1 -b .replace_aquapopupmenuui
dos2unix src/com/jidesoft/utils/DateUtils.java
dos2unix src/com/jidesoft/swing/CheckBoxListWithSelectable.java
%patch2 -p2
unix2dos src/com/jidesoft/utils/DateUtils.java
unix2dos src/com/jidesoft/swing/CheckBoxListWithSelectable.java

%build
%ant javadoc jar

%install
install -D -p -m 644 %{name}-%{version}.jar \
	%{buildroot}%{_javadir}/%{name}-%{version}.jar

install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -rf -p javadoc/* %{buildroot}%{_javadocdir}/%{name}

pushd %{buildroot}%{_javadir}
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd

%files
%doc LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%files doc
%doc docs/JIDE_Common_Layer_Developer_Guide.pdf

%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_7.1340svnjpp7
- new version

