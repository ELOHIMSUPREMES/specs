# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global install_loc    %{_datadir}/eclipse/dropins/jgit
%global version_suffix 201212191850-r

Name:           eclipse-jgit
Version:        2.2.0
Release:        alt1_1jpp7
Summary:        Eclipse JGit

Group:          Development/Java
License:        BSD
URL:            http://www.eclipse.org/egit/
Source0:        http://git.eclipse.org/c/jgit/jgit.git/snapshot/jgit-%{version}.%{version_suffix}.tar.bz2
Patch0:         fix_jgit_sh.patch

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.5.0
BuildRequires:  jpackage-utils
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-shade-plugin
BuildRequires:  args4j >= 2.0.12
BuildRequires:	apache-commons-compress
BuildRequires:       xz-java >= 1.1-2
Requires: eclipse-platform >= 3.5.0
Source44: import.info

%description
A pure Java implementation of the Git version control system.

%package -n     jgit-javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description -n jgit-javadoc
%{summary}.

%package -n     jgit
Summary:        Java-based command line Git interface
Group:          Development/Java
Requires:       args4j >= 2.0.12
Requires:       apache-commons-compress
Requires:       xz-java >= 1.1-2
Requires:       jpackage-utils

%description -n jgit
Command line Git tool built entirely in Java.

%prep
%setup -n jgit-%{version}.%{version_suffix} -q
sed -i -e "s|\${bundle-manifest}|\${source-bundle-manifest}|g" \
 org.eclipse.jgit/pom.xml org.eclipse.jgit.ui/pom.xml  org.eclipse.jgit.console/pom.xml \
 org.eclipse.jgit.iplog/pom.xml org.eclipse.jgit.iplog/pom.xml org.eclipse.jgit.pgm/pom.xml

%patch0

find . -name MANIFEST.MF -exec sed -i -e 's|7.6.0,8.0.0|7.6.0,8.6.0|g' {} \;
sed -i -e 's|org.kohsuke.args4j|args4j|g' org.eclipse.jgit.packaging/org.eclipse.jgit.orbit.feature/feature.xml
%build
mkdir -p deps/plugins
pushd deps/
	ln -s %{_javadir}/commons-compress.jar
	ln -s %{_javadir}/xz-java.jar
	ln -s %{_javadir}/args4j.jar
popd

# build plugin
%{_bindir}/eclipse-pdebuild -f org.eclipse.jgit -o `pwd`/deps
# build JARs
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -Dtranslate-qualifier=true install \
 -pl "org.eclipse.jgit,org.eclipse.jgit.ui,org.eclipse.jgit.console,org.eclipse.jgit.iplog,org.eclipse.jgit.pgm"

%install
install -d -m 755 %{buildroot}%{install_loc}
# Eclipse Plugin
%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.jgit.zip
pushd %{buildroot}%{install_loc}/eclipse/plugins
	rm args4j_*.jar
	rm com.jcraft.jsch_*.jar
	rm org.apache.commons.compress_*.jar
	ln -s %{_javadir}/args4j.jar
	ln -s %{_javadir}/commons-compress.jar
	ln -s %{_javadir}/xz-java.jar
popd

# JARs
install -d -m 0755 %{buildroot}%{_javadir}/jgit
install -m 644 org.eclipse.jgit/target/org.eclipse.jgit-%{version}.%{version_suffix}.jar   %{buildroot}%{_javadir}/jgit/jgit.jar
install -m 644 org.eclipse.jgit.ui/target/org.eclipse.jgit.ui-%{version}.%{version_suffix}.jar   %{buildroot}%{_javadir}/jgit/ui.jar
install -m 644 org.eclipse.jgit.console/target/org.eclipse.jgit.console-%{version}.%{version_suffix}.jar   %{buildroot}%{_javadir}/jgit/console.jar
install -m 644 org.eclipse.jgit.iplog/target/org.eclipse.jgit.iplog-%{version}.%{version_suffix}.jar   %{buildroot}%{_javadir}/jgit/iplog.jar
install -m 644 org.eclipse.jgit.pgm/target/org.eclipse.jgit.pgm-%{version}.%{version_suffix}.jar   %{buildroot}%{_javadir}/jgit/pgm.jar
# Javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/jgit
cp -rp org.eclipse.jgit/target/apidocs %{buildroot}%{_javadocdir}/jgit
cp -rp org.eclipse.jgit.ui/target/apidocs %{buildroot}%{_javadocdir}/jgit
cp -rp org.eclipse.jgit.console/target/apidocs %{buildroot}%{_javadocdir}/jgit
cp -rp org.eclipse.jgit.iplog/target/apidocs %{buildroot}%{_javadocdir}/jgit
# POM Files
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-jgit-parent.pom
install -pm 644 org.eclipse.jgit/pom.xml %{buildroot}%{_mavenpomdir}/JPP.jgit-jgit.pom
install -pm 644 org.eclipse.jgit.ui/pom.xml %{buildroot}%{_mavenpomdir}/JPP.jgit-ui.pom
install -pm 644 org.eclipse.jgit.console/pom.xml %{buildroot}%{_mavenpomdir}/JPP.jgit-console.pom
install -pm 644 org.eclipse.jgit.iplog/pom.xml %{buildroot}%{_mavenpomdir}/JPP.jgit-iplog.pom
install -pm 644 org.eclipse.jgit.pgm/pom.xml %{buildroot}%{_mavenpomdir}/JPP.jgit-pgm.pom

%add_maven_depmap JPP.jgit-jgit.pom jgit/jgit.jar
%add_maven_depmap JPP.jgit-ui.pom jgit/ui.jar
%add_maven_depmap JPP.jgit-console.pom jgit/console.jar
%add_maven_depmap JPP.jgit-iplog.pom jgit/iplog.jar
%add_maven_depmap JPP.jgit-pgm.pom jgit/pgm.jar
%add_maven_depmap JPP-jgit-parent.pom
# Binary
install -dm 755 %{buildroot}%{_bindir}
install -m 755 org.eclipse.jgit.pgm/jgit.sh %{buildroot}%{_bindir}/jgit

%files
%doc LICENSE 
%doc README.md
%{install_loc}

%files -n jgit
%{_bindir}/jgit
%{_javadir}/jgit
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-jgit-parent.pom
%{_mavenpomdir}/JPP.jgit*.pom
%doc LICENSE 
%doc README.md

%files -n jgit-javadoc
%{_javadocdir}/jgit
%doc LICENSE 
%doc README.md

%changelog
* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_2jpp7
- fixed build

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_2jpp7
- new version

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1jpp6
- update to new release by jppimport

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_1jpp6
- new version

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_0.1.git20091029jpp6
- new version

