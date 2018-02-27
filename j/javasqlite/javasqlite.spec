Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: libsqlite-devel
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name javasqlite
%define version 20130214
# javaver nil: build for 1.5.0 and 1.6.0
# javaver something else: build only for that

%if 0%{?fedora} > 16
# Java >= 1.7.0 stuff can't coexist in jar with older versions
%global javaver 1.7.0
%endif

%if 0%{?el6}
%ifarch ppc64
# No Java >= 1.6.0 available for EL6 ppc64 as of 20120225
%global javaver 1.5.0
%endif
%endif

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\.so$

Name:           javasqlite
Version:        20130214
Release:        alt1_1jpp7
Summary:        SQLite Java Wrapper/JDBC Driver

License:        BSD
URL:            http://www.ch-werner.de/javasqlite/
Source0:        http://www.ch-werner.de/javasqlite/%{name}-%{version}.tar.gz
# Fedora specific, no need to send upstream.
Patch0:         %{name}-20090430-jnipath.patch

# >= 3.4 for zeroblob stuff in %%check's test3
BuildRequires:  libsqlite3-devel >= 3.4
%if 0%{?javaver:1}
BuildRequires:  java-%{javaver}-devel
BuildRequires:  java-%{javaver}-javadoc
Requires:       jre-%{javaver}
%else
BuildRequires:  java-1.6.0-javadoc
Requires:       jre >= 1.5.0
%endif
%ifarch aarch64 #925605
BuildRequires:  libtool
%endif
Source44: import.info

%description
javasqlite is a Java wrapper including a basic JDBC driver for the
SQLite database engine. It is designed using JNI to interface to the
SQLite API.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
BuildArch:      noarch
Requires:       java-javadoc

%description    javadoc
API documentation for %{name}.


%prep
%setup -q
sed -e 's|@JNIPATH@|%{_libdir}/%{name}|' %{PATCH0} | patch -p1 --fuzz=0
sed -i -e 's/\r//g' doc/ajhowto.txt
f=ChangeLog ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f
%ifarch aarch64 #925605
autoreconf -if
%endif


%build

origpath="$PATH"
# Note that --enable-load-extension has security concerns, see configure --help
common_flags="
    --with-jardir=%{_libdir}/%{name}
    --libdir=%{_libdir}/%{name}
"

%if 0%{?javaver:1}

export PATH="%{_jvmdir}/java-%{javaver}/bin:$origpath" # bug 460761
%configure $common_flags --with-jdk=%{_jvmdir}/java-%{javaver}
make sqlite.jar # Java build not parallel clean
make %{?_smp_mflags}

%else

# We build both JDBC 3 and 4 drivers here so the resulting jar includes both,
# and in a way that the classfiles are usable with both Java 1.5 and 1.6.
# The idea is to first build the JDBC 3 driver and common files with Java 1.5,
# then JDBC 4 and remaining files with Java 1.6, the desired result being that
# the Java 1.6 build will not recompile the common class files that were
# previously built with 1.5.

# Pass #1: JDBC 3 driver and common files with 1.5.0
export PATH="%{_jvmdir}/java-1.5.0/bin:$origpath" # bug 460761
%configure $common_flags --with-jdk=%{_jvmdir}/java-1.5.0
make sqlite.jar JAVAC_FLAGS="-source 5" # Java build not parallel clean

# Pass #2: JDBC 4 driver and the rest with 1.6.0
export PATH="%{_jvmdir}/java-1.6.0/bin:$origpath" # bug 460761 (to be sure)
%configure $common_flags --with-jdk=%{_jvmdir}/java-1.6.0
make # Java build not parallel clean

# Add JDBC 3 classes
jar uf sqlite.jar SQLite/JDBC2y/*.class

%endif

make javadoc JAVADOCLINK=%{_javadocdir}/java


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/libsqlite_jni.la
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pR doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%check
origpath="$PATH"
for javaver in %{?javaver} %{!?javaver:1.5.0 1.6.0} ; do
    jdir=%{_jvmdir}/java-$javaver/bin
    export PATH="$jdir:$origpath" # bug 460761
    # test2 is for SQLite 2.x, which we don't support
    make JAVA_RUN="$jdir/java" JAVAC="$jdir/javac" test test3 testg
done


%files
%doc ChangeLog license.terms
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/sqlite.jar
%{_libdir}/%{name}/libsqlite_jni.so

%files javadoc
%doc license.terms
%{_javadocdir}/%{name}


%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 20130214-alt1_1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 20120209-alt1_2jpp7
- new version

