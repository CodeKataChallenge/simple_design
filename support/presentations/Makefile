.PHONY: all, clean

SOURCE_DIR=src
BUILD_DIR=../../docs/js
SOURCE=${SOURCE_DIR}/Presentations.elm
ELM_CODE=$(shell find ${SOURCE_DIR} -name '*.elm')
TARGET=${BUILD_DIR}/p.js
MINIFIED_TARGET=${BUILD_DIR}/p.min.js

all: ${MINIFIED_TARGET}
	@echo "finished"

${MINIFIED_TARGET}: ${TARGET} 
	uglifyjs $< --compress "pure_funcs=[F2,F3,F4,F5,F6,F7,F8,F9,A2,A3,A4,A5,A6,A7,A8,A9],pure_getters,keep_fargs=false,unsafe_comps,unsafe" | uglifyjs --mangle --output $@

${TARGET}: ${SOURCE} ${ELM_CODE}
	elm make $< --optimize --output $@

clean:
	rm -f ${TARGET} ${MINIFIED_TARGET}