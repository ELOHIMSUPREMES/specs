Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-marshalling
%define version 1.4.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-marshalling
Version:          1.4.1
Release:          alt1_1jpp7
Summary:          JBoss Marshalling
License:          LGPLv2+
URL:              http://www.jboss.org/jbossmarshalling
BuildArch:        noarch

Source0:          https://github.com/jboss-remoting/jboss-marshalling/archive/%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    jboss-parent
BuildRequires:    jboss-modules
BuildRequires:    maven-injection-plugin
%if 0%{?fedora}
BuildRequires:    apiviz
%endif
Source44: import.info

%description
JBoss Marshalling is an alternative serialization API that fixes many
of the problems found in the JDK serialization API while remaining
fully compatible with java.io.Serializable and its relatives, and adds
several new tunable parameters and additional features, all of which
are pluggable via factory configuration (externalizers, class/instance
lookup tables, class resolution, and object replacement, to name a
few).

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin :maven-shade-plugin
%pom_disable_module tests
%pom_disable_module osgi

# Compat symlinks.  TODO: remove once jboss-as is rebuilt to use the
# new JAR names.
%mvn_file :{*} %{name}/@1 @1

# Conditionally remove dependency on apiviz
if [ %{?rhel} ]; then
    %pom_remove_plugin :maven-javadoc-plugin
fi

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc COPYING.txt

%files javadoc -f .mfiles-javadoc
%doc COPYING.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt1_3jpp7
- new version

