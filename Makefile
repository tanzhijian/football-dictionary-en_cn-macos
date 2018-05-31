# Makefile

# 设置
DICT_NAME		=	"Football Terms Dictionary"
DICT_SRC_PATH		=	converter/data.xml
CSS_PATH		=	converter/style.css
PLIST_PATH		=	converter/info.plist

DICT_BUILD_OPTS		=

# DICT_BUILD_TOOL_DIR 的值改为你的 Dictionary Development Kit 位置
DICT_BUILD_TOOL_DIR	=	"/Applications/Utilities/Dictionary Development Kit"
DICT_BUILD_TOOL_BIN	=	"$(DICT_BUILD_TOOL_DIR)/bin"

# Python 位置
PYTHON_PATH = "$(HOME)/myvenv/football-dictionary-en_cn-macos/bin/python"
CONVERTER = "$(shell pwd)/converter/convert.py"

# 测试
NOSE = "$(HOME)/myvenv/football-dictionary-en_cn-macos/bin/nosetests"
TESTS = "$(shell pwd)/tests"

###########################

DICT_DEV_KIT_OBJ_DIR	=	./objects
export	DICT_DEV_KIT_OBJ_DIR

DESTINATION_FOLDER	=	~/Library/Dictionaries
RM			=	/bin/rm

###########################

all:
	echo "Converting."
	$(PYTHON_PATH) $(CONVERTER)
	"$(DICT_BUILD_TOOL_BIN)/build_dict.sh" $(DICT_BUILD_OPTS) $(DICT_NAME) $(DICT_SRC_PATH) $(CSS_PATH) $(PLIST_PATH)
	echo "Done."


install:
	echo "Installing into $(DESTINATION_FOLDER)".
	mkdir -p $(DESTINATION_FOLDER)
	ditto --noextattr --norsrc $(DICT_DEV_KIT_OBJ_DIR)/$(DICT_NAME).dictionary  $(DESTINATION_FOLDER)/$(DICT_NAME).dictionary
	touch $(DESTINATION_FOLDER)
	echo "Done."
	echo "To test the new dictionary, try Dictionary.app."


clean:
	$(RM) -rf $(DICT_DEV_KIT_OBJ_DIR)
	$(RM) $(DICT_SRC_PATH)


test:
	$(NOSE) $(TESTS)
