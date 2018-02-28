%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
#
# spec file for package svgsalamander

Name:           svgsalamander
Version:        0.1.33
Release:        alt1_2jpp8
Summary:        An SVG engine for Java

Group:          Development/Java
License:        LGPLv2+ or BSD
URL:            http://svgsalamander.java.net/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-generate-tarball.sh
#Source built using the following commands : sh svgSalamander-generate-tarball.sh

BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  javacc-maven-plugin
BuildRequires:  maven-enforcer-plugin
Source44: import.info


%description
SVG Salamander is an SVG engine for Java that's designed to be small, fast, 
and allow programmers to use it with a minimum of fuss. It's in particular 
targeted for making it easy to integrate SVG into Java games and making it 
much easier for artists to design 2D game content - from rich interactive 
menus to charts and graphcs to complex animations.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find . -name '*.jar' -exec rm -f '{}' \;
find . -name '*.class' -exec rm -f '{}' \;

# Remove DOS line endings
for file in www/docs/*.html www/docs/exampleCode/*.html; do
  sed 's|\r||g' $file >$file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done


%build
pushd svg-core
%mvn_file : %{name} svgSalamander svg-salamander
%mvn_alias : com.kitfox.svg:svg-salamander
%mvn_build
popd

%install
pushd svg-core
%mvn_install
popd

%files -f svg-core/.mfiles
%doc www/docs/{exampleCode/,use.html}
%doc www/license/*

%files javadoc -f svg-core/.mfiles-javadoc
%doc www/license/*

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.33-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.19-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.10-alt1_3jpp7
- new release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.10-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_2jpp7
- new version

