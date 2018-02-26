# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           OpenStego
Version:        0.5.2
Release:        alt2_9jpp7
Summary:        Free Steganography solution
Group:          File tools
License:        GPLv2
URL:            http://openstego.sourceforge.net/index.html
Source0:        http://downloads.sourceforge.net/project/openstego/openstego/openstego-%{version}/openstego-src-%{version}.zip
Source1:        openstego.desktop
BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  desktop-file-utils
Requires:       jpackage-utils
Source44: import.info

%description
OpenStego is a tool implemented in Java for generic steganography,
with support for password-based encryption of the data. It supports
plugins for various steganographic algorithms.

%package javadoc
Group:     Development/Java
BuildArch: noarch
Requires:  jpackage-utils
Summary:   Javadoc generated documentation for Openstego

%description javadoc
Javadoc generated documentation for Openstego.


%prep
%setup -q -n openstego-src-%{version}
find . -name *.class -delete
find . -name *.jar -delete
# Delete file for Windows :
rm -f openstego.bat


%build
ant package doc


%install
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_javadocdir}/openstego
cp -p ./lib/openstego.jar %{buildroot}%{_javadir}/openstego.jar
cp -p ./src/image/ImagesVectorSource.svg %{buildroot}%{_datadir}/pixmaps/openstego.svg
cp -pr ./doc/api/* %{buildroot}%{_javadocdir}/openstego
%jpackage_script net.sourceforge.openstego.OpenStego "" "" openstego.jar openstego true
# Install openstego.desktop :
desktop-file-install                       \
--dir=%{buildroot}%{_datadir}/applications \
%{SOURCE1}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/OpenStego.conf`
touch $RPM_BUILD_ROOT/etc/java/OpenStego.conf


%files
%doc README LICENSE
%{_bindir}/openstego
%{_javadir}/openstego.jar
%{_datadir}/pixmaps/openstego.svg
%{_datadir}/applications/openstego.desktop
%config(noreplace,missingok) /etc/java/OpenStego.conf

%files javadoc
%doc LICENSE
%{_javadocdir}/openstego/


%changelog
* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_9jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_9jpp7
- new version

