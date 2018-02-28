Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name codegen
%define version 0.6.7
%global _version %( echo %{version} | tr . _ )
Name:          codegen
Version:       0.6.7
Release:       alt1_1jpp8
Summary:       Java/Scala Code generation tool
License:       ASL 2.0
URL:           http://www.querydsl.com
Source0:       https://github.com/mysema/codegen/archive/CODEGEN_%{_version}.tar.gz
# https://github.com/querydsl/codegen/issues/22
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
# https://bugzilla.redhat.com/show_bug.cgi?id=1015787
BuildRequires: mvn(org.eclipse.jdt.core.compiler:ecj)

BuildArch:     noarch
Source44: import.info

%description
Code generation and compilation for Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-CODEGEN_%{_version}

%pom_remove_parent
%pom_remove_plugin com.springsource.bundlor:com.springsource.bundlor.maven
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<configuration>
 <instructions>
  <Bundle-Name>Codegen</Bundle-Name>
  <Bundle-SymbolicName>com.mysema.codegen</Bundle-SymbolicName>
  <Bundle-Vendor>Mysema</Bundle-Vendor>
  <Export-Package>com.mysema.codegen*;version="${project.version}"</Export-Package>
  <Import-Package>
    javax.annotation.*;version="0",
    javax.tools.*;version="0",
    org.eclipse.jdt.*;version="3.7.2",
    com.google.common.*;version="${guava.version}",
    *
  </Import-Package>
 </instructions>
</configuration>
<executions>
 <execution>
  <id>bundle-manifest</id>
  <phase>process-classes</phase>
  <goals>
    <goal>manifest</goal>
  </goals>
 </execution>
</executions>'

%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:useDefaultManifestFile"
%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration" '
<archive>
 <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
</archive>'

sed -i.javax.validation "s|ConstraintPayload|Payload|" \
 src/test/java/com/mysema/codegen/MaxImpl.java \
 src/test/java/com/mysema/codegen/MinImpl.java \
 src/test/java/com/mysema/codegen/NotNullImpl.java

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

%mvn_file com.mysema.codegen:%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_1jpp8
- java 8 mass update

