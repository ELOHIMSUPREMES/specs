# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global project_version 1.0-beta-2

Name:           plexus-active-collections
Version:        1.0
Release:        alt2_0.12.beta2jpp7
Summary:        Plexus Container-Backed Active Collections

Group:          Development/Java
License:        ASL 2.0
URL:            http://plexus.codehaus.org/
#svn export http://svn.codehaus.org/plexus/tags/plexus-active-collections-1.0-beta-2/
#tar zcf plexus-active-collections-1.0-beta-2.tar.gz plexus-active-collections-1.0-beta-2/
Source0:        plexus-active-collections-1.0-beta-2.tar.gz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt

Patch0:         %{name}-migration-to-component-metadata.patch

BuildArch: noarch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  ant
BuildRequires:  maven-local
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-component-api
BuildRequires:  junit

Requires:          plexus-component-api
Requires:          plexus-containers-container-default
Requires:          plexus-utils
Requires:          junit
Requires:          jpackage-utils
Source44: import.info


%description
Plexus Container-Backed Active Collections

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{project_version}
%patch0 -p1
cp %{SOURCE1} .

%build
mvn-rpmbuild \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/plexus
install -m 644 target/%{name}-%{project_version}.jar %{buildroot}%{_javadir}/plexus/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.plexus-%{name}.pom 
%add_maven_depmap JPP.plexus-%{name}.pom plexus/%{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/plexus/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/plexus/%{name}/

%files
%doc LICENSE-2.0.txt
%{_javadir}/plexus/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE-2.0.txt
%{_javadocdir}/plexus/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.12.beta2jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.9.beta2jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.9.beta2jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.8.beta2jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.7.beta2jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

