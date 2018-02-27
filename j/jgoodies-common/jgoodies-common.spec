# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global shortname common

Name:           jgoodies-common
Version:        1.6.0
Release:        alt1_3jpp7
Summary:        Common library shared by JGoodies libraries and applications

Group:          Development/Java
License:        BSD
URL:            http://www.jgoodies.com/
Source0:        http://www.jgoodies.com/download/libraries/%{shortname}/%{name}-%(tr "." "_" <<<%{version}).zip

# fontconfig and DejaVu fonts needed for tests
BuildRequires:  fonts-ttf-dejavu
BuildRequires:  fontconfig
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-dependency-plugin
Requires:       jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
The JGoodies Common library provides convenience code for other JGoodies
libraries and applications.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q

# Unzip source and test files from provided JARs
mkdir -p src/main/java/ src/test/java/
pushd src/main/java/
jar -xf ../../../%{name}-%{version}-sources.jar
popd
pushd src/test/java/
jar -xf ../../../%{name}-%{version}-tests.jar
popd

# Delete prebuild JARs
find -name "*.jar" -exec rm {} \;

# Remove DOS line endings
for file in LICENSE.txt RELEASE-NOTES.txt; do
  sed 's|\r||g' $file > $file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done

%mvn_file :%{name} %{name} %{name}


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt README.html RELEASE-NOTES.txt


%files javadoc -f .mfiles-javadoc


%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_3jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_1jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1jpp7
- initial build

