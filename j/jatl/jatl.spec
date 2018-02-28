Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jatl
Version:       0.2.2
Release:       alt1_7jpp8
Summary:       Java Anti-Template Language
License:       ASL 2.0
# https://github.com/agentgt
URL:           https://github.com/chris-martin/jatl
Source0:       https://github.com/chris-martin/jatl/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(commons-lang:commons-lang)
# test deps
BuildRequires: mvn(junit:junit)

Requires:      mvn(commons-lang:commons-lang)

BuildArch:     noarch
Source44: import.info

%description
Is an extremely lightweight efficient Java library to
generate XHTML or XML in a micro DSL builder/fluent style.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Unwanted
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin :maven-license-plugin
# Unwanted build source jar
%pom_remove_plugin :maven-source-plugin
# Unwanted build javadoc jar
%pom_remove_plugin :maven-javadoc-plugin
# Unavailable
%pom_remove_plugin com.googlecode.maven-gcu-plugin:maven-gcu-plugin

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc COPYING

%files javadoc -f .mfiles-javadoc
%doc COPYING

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_7jpp8
- new version

