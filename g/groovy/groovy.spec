Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-compat
# Note to packagers: When rebasing this to a later version, do not
# forget to ensure that sources 1 and 2 are up to date as well as
# the Requires list.

Name:           groovy
Version:        1.8.9
Release:        alt1_5jpp7
Summary:        Dynamic language for the Java Platform

Group:          Development/Java
# Some of the files are licensed under BSD and CPL terms, but the CPL has been superceded
# by the EPL. We include copies of both for completeness.
# groovyConsole uses CC-BY licensed icons
# (see: subprojects/groovy-console/target/tmp/groovydoc/groovy/ui/icons/credits.txt)
License:        ASL 2.0 and BSD and EPL and Public Domain and CC-BY
URL:            http://groovy.codehaus.org/
Source0:        http://dist.groovy.codehaus.org/distributions/%{name}-src-%{version}.zip
Source1:        groovy-script
Source2:        groovy-starter.conf
Source3:        groovy.desktop
Source4:        cpl-v10.txt
Source5:        epl-v10.txt
Source6:        http://www.apache.org/licenses/LICENSE-2.0.txt
# http://jira.codehaus.org/browse/GROOVY-6085
Patch0:         groovy-inner-interface-annotations.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  antlr-tool
BuildRequires:  ant-antlr
BuildRequires:  objectweb-asm
BuildRequires:  bsf
BuildRequires:  apache-ivy
BuildRequires:  jansi
BuildRequires:  jline
BuildRequires:  tomcat-jsp-2.2-api
BuildRequires:  junit
BuildRequires:  tomcat-servlet-3.0-api
BuildRequires:  xstream
BuildRequires:  desktop-file-utils
BuildRequires:  jpackage-utils
BuildRequires:  apache-commons-cli
BuildRequires:  unzip
BuildRequires:  ecj
Requires:       jpackage-utils

# The are all runtime dependencies of the script
# TODO: Think of splitting them into a separate subpackage
Requires:       ant
Requires:       ant-junit
Requires:       antlr-tool
Requires:       objectweb-asm
Requires:       bsf
Requires:       apache-commons-cli
Requires:       apache-commons-logging
Requires:       apache-ivy
Requires:       jansi
Requires:       jline
Requires:       tomcat-jsp-2.2-api
Requires:       junit
Requires:       tomcat-servlet-3.0-api
Requires:       xstream
Source44: import.info


%description
Groovy is an agile and dynamic language for the Java Virtual Machine,
built upon Java with features inspired by languages like Python, Ruby and
Smalltalk.  It seamlessly integrates with all existing Java objects and
libraries and compiles straight to Java bytecode so you can use it anywhere
you can use Java.


%package javadoc
Summary:        API Documentation for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch
%description javadoc
JavaDoc documentation for %{name}


%prep
%setup -q
cp %{SOURCE4} %{SOURCE5} %{SOURCE6} .
# Remove bundled JARs and classes
find \( -name *.jar -o -name *.class \) -delete

%patch0 -p1

%build
mkdir -p target/lib/{compile,tools}

# Construct classpath
build-jar-repository target/lib/compile servlet jsp \
        objectweb-asm/asm-tree objectweb-asm/asm \
        objectweb-asm/asm-util objectweb-asm/asm-analysis \
        antlr ant/ant-antlr antlr \
        bsf jline xstream ant junit ivy commons-cli \
        jansi

# Use ECJ instead of OpenJDK to compile MethodHandle.  This is a
# workaround for a bug in OpenJDK that causes compilation of
# MethodHandle to take many minutes (15min or even more), while ECJ
# can compile it under five seconds.  See rhbz#971483 and
# http://mail.openjdk.java.net/pipermail/compiler-dev/2013-May/006339.html
ecj -d target/classes `find -name MethodHandle.java -o -name ArrayUtil.java`

# Build
# TODO: Build at least tests, maybe examples
ant -DskipTests=on -DskipExamples=on -DskipFetch=on -DskipEmbeddable=on \
        createJars javadoc


%install

# Code
install -d $RPM_BUILD_ROOT%{_javadir}
install -p -m644 target/dist/groovy.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Startup scripts
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/groovy
for TOOL in grape groovyc groovyConsole java2groovy groovysh
do
        ln $RPM_BUILD_ROOT%{_bindir}/groovy \
                $RPM_BUILD_ROOT%{_bindir}/$TOOL
done

# Configuration
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m644 %{SOURCE2} \
        $RPM_BUILD_ROOT%{_sysconfdir}/groovy-starter.conf

# Desktop icon
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -d $RPM_BUILD_ROOT%{_datadir}/applications
install -p -m644 src/main/groovy/ui/ConsoleIcon.png \
        $RPM_BUILD_ROOT%{_datadir}/pixmaps/groovy.png
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        %{SOURCE3}

# API Documentation
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
find target -type d |xargs chmod 755
cp -rp target/html/api/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Maven depmap
install -d $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p $RPM_BUILD_ROOT`dirname /etc/groovy.conf`
touch $RPM_BUILD_ROOT/etc/groovy.conf

%files
%{_bindir}/*
%{_javadir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*
%config(noreplace) %{_sysconfdir}/*
%doc README.md
%doc LICENSE.txt LICENSE-2.0.txt NOTICE.txt cpl-v10.txt epl-v10.txt
%config(noreplace,missingok) /etc/groovy.conf


%files javadoc
%{_javadocdir}/*
%doc LICENSE.txt LICENSE-2.0.txt NOTICE.txt cpl-v10.txt epl-v10.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.9-alt1_5jpp7
- new release

* Sun Jul 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.9-alt1_2jpp7
- update

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.7-alt1_1jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.6-alt2_2jpp7
- applied repocop patches

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.6-alt1_2jpp7
- new version

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_2jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_2jpp5
- use maven1

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp5
- selected java5 compiler explicitly

* Sun May 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- disabled rebuild-java-repository

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Sat Nov 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

