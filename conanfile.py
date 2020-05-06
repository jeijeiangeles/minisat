from conans import ConanFile, tools


class MinisatConan(ConanFile):
    python_requires = "conan_base/[~=1]@cybercalc+ci-scripts/master"
    python_requires_extend = "conan_base.CybercalcConanBase"

    name = "minisat"
    url = "https://demeeslx0105/cybercalc/external-deps/minisat"
    homepage = url
    author = "Niklas Sorensson <niklasso@gmail.com>"
    description = "A minimalistic and high-performance SAT solver"
    license = "MIT"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto",
    }

    def source(self):
        tools.replace_in_file("CMakeLists.txt", "project(MiniSat VERSION 2.2 LANGUAGES CXX)",
                              '''project(MiniSat VERSION 2.2 LANGUAGES CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = self.CMake()
        cmake.configure()
        cmake.build()
        if self.should_test:
            self.run('ctest -j `nproc`')

    def package(self):
        cmake = self.CMake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs += ['minisat']
