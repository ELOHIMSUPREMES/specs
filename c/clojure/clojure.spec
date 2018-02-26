BuildRequires: /proc
BuildRequires: jpackage-compat
%global project     clojure
%global groupId     org.clojure
%global artifactId  clojure
%global archivename %{project}-%{artifactId}
%global commit_hash 0ba3ff1

Name:           clojure
Epoch:          1
Version:        1.4.0
Release:        alt1_3jpp7
Summary:        A dynamic programming language that targets the Java Virtual Machine

Group:          Development/Java
License:        EPL
URL:            http://clojure.org/
# wget --content-disposition \
#   https://github.com/clojure/clojure/tarball/clojure-%{version}
Source0:        %{project}-%{archivename}-%{version}-0-g%{commit_hash}.tar.gz

Source1:        clojure.sh

BuildArch:      noarch

BuildRequires:  ant >= 1.6
BuildRequires:  jpackage-utils >= 1.5
BuildRequires:  objectweb-asm

Requires:       jpackage-utils
Requires:       objectweb-asm
Source44: import.info

%description 
Clojure is a dynamic programming language that targets the Java
Virtual Machine. It is designed to be a general-purpose language,
combining the approachability and interactive development of a
scripting language with an efficient and robust infrastructure for
multithreaded programming. Clojure is a compiled language - it
compiles directly to JVM bytecode, yet remains completely
dynamic. Every feature supported by Clojure is supported at
runtime. Clojure provides easy access to the Java frameworks, with
optional type hints and type inference, to ensure that calls to Java
can avoid reflection.

%prep
%setup -q -n %{archivename}-8306949

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 

%install
# jar - link to prefix'd jar so that java stuff knows where to look
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# startup script
install -d -m 755 %{buildroot}%{_bindir}
install -pm 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%if 0%{?add_maven_depmap:1}
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%else
# some systems like RHEL do not have add_maven_depmap defined
# - probably don't need JPP/%{name} -- do we?
%add_to_maven_depmap %{groupId} %{artifactId} %{version} JPP %{name}
%endif

%files
%doc epl-v10.html changes.md readme.txt 
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}.jar
%{_bindir}/%{name}

%changelog
* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_3jpp7
- new release

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.3.0-alt1_1jpp6
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_1jpp6
- update to new release by jppimport

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.2.0-alt1_1jpp6
- new version (closes: #24726)

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 20080916-alt1_2jpp5
- first build

