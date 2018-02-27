# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           plexus-sec-dispatcher
Version:        1.4
Release:        alt2_11jpp7
Summary:        Plexus Security Dispatcher Component

Group:          Development/Java
License:        ASL 2.0
URL:            http://spice.sonatype.org
#svn export http://svn.sonatype.org/spice/tags/plexus-sec-dispatcher-1.4/
#tar jcf plexus-sec-dispatcher-1.4.tar.bz2 plexus-sec-dispatcher-1.4/
Source0:        %{name}-%{version}.tar.bz2
#Removed maven-compiler-plugin configuration version in the pom as annotations isn't available in version 1.4.
Patch0:        %{name}-pom.patch

BuildArch: noarch

BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-maven-plugin
BuildRequires: plexus-utils
BuildRequires: plexus-cipher
BuildRequires: plexus-containers-component-metadata
BuildRequires: junit
BuildRequires: forge-parent
BuildRequires: spice-parent
BuildRequires: maven-surefire-provider-junit

Requires:       jpackage-utils
Source44: import.info

%description
Plexus Security Dispatcher Component

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1

%build
mvn-rpmbuild install javadoc:javadoc

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/plexus/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.plexus-%{name}.pom

%add_maven_depmap JPP.plexus-%{name}.pom plexus/%{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/plexus/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/plexus/%{name}

%files
%{_javadir}/plexus/*
%{_mavenpomdir}/JPP.plexus-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/plexus/%{name}

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_10jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_7jpp7
- fixed build

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

