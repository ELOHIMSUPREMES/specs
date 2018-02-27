Epoch: 1
BuildRequires: /proc
BuildRequires: jpackage-compat
%global short_name      commons-validator

Name:             apache-%{short_name}
Version:          1.4.0
Release:          alt1_6jpp7
Summary:          Apache Commons Validator
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/validator/
Source0:          http://www.apache.org/dist/commons/validator/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    apache-commons-beanutils
BuildRequires:    apache-commons-digester
BuildRequires:    apache-commons-logging
BuildRequires:    maven-local
Requires:         jpackage-utils
Source44: import.info

%description
A common issue when receiving data either electronically or from user input is
verifying the integrity of the data. This work is repetitive and becomes even
more complicated when different sets of validation rules need to be applied to
the same set of data based on locale for example. Error messages may also vary
by locale. This package attempts to address some of these issues and speed
development and maintenance of validation rules.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :commons-validator %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_6jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_4jpp7
- new version

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1_9jpp7
- fc update

* Sat Sep 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_0.r832761.5jpp6
- marked oro as essential dependency due to maven-site-plugin

* Sat Feb 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_0.r832761.5jpp6
- new version

