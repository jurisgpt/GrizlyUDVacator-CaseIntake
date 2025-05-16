# Streamlit Static Analysis Report
Generated: 2025-05-15 15:33:50

## Tools Summary
- **pylint** (🔥 Essential): ✓ Ran successfully
- **mypy** (✅ Very helpful): ✓ Ran successfully
- **bandit** (✅ Important): ✓ Ran successfully
- **vulture** (⚠️ Nice to have): ✓ Ran successfully
- **flake8** (✅ Helps with readability): ✓ Ran successfully

## 🔥 Streamlit-Specific Issues
- **vulture** (.venv/lib/python3.11/site-packages/altair/expr/__init__.py:750): unused method 'sampleUniform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/expr/__init__.py:765): unused method 'cumulativeUniform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/expr/__init__.py:784): unused method 'densityUniform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/expr/__init__.py:803): unused method 'quantileUniform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/expr/__init__.py:1297): unused method 'dayFormat' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/expr/__init__.py:1306): unused method 'dayAbbrevFormat' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/expr/__init__.py:1328): unused method 'monthFormat' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/expr/__init__.py:1337): unused method 'monthAbbrevFormat' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/expr/__init__.py:1404): unused method 'utcFormat' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/expr/__init__.py:1971): unused method 'containerSize' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:2563): unused method 'transform_aggregate' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:2641): unused method 'transform_bin' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:2701): unused method 'transform_calculate' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:2770): unused method 'transform_density' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:2848): unused method 'transform_impute' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:2918): unused method 'transform_joinaggregate' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:2974): unused method 'transform_extent' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:2995): unused method 'transform_filter' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3103): unused method 'transform_flatten' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3136): unused method 'transform_fold' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3164): unused method 'transform_loess' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3207): unused method 'transform_lookup' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3261): unused method 'transform_pivot' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3308): unused method 'transform_quantile' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3355): unused method 'transform_regression' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3423): unused method 'transform_sample' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3443): unused method 'transform_stack' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3485): unused method 'transform_timeunit' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/api.py:3568): unused method 'transform_window' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/altair/vegalite/v5/schema/mixins.py:1578): unused method 'configure_tooltipFormat' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/astroid/interpreter/objectmodel.py:477): unused variable 'attr___format__' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/astroid/interpreter/objectmodel.py:886): unused property 'attr_keys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/astroid/nodes/as_string.py:320): unused method 'visit_formattedvalue' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/astroid/rebuilder.py:1258): unused method 'visit_formattedvalue' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/bandit/core/tester.py:13): unused attribute 'formatwarning' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/bandit/plugins/ssh_no_host_key_verification.py:45): unused function 'ssh_no_host_key_verification' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/bandit/plugins/weak_cryptographic_key.py:159): unused function 'weak_cryptographic_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/charset_normalizer/md.py:165): unused class 'SuspiciousDuplicateAccentPlugin' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/charset_normalizer/md.py:480): unused class 'ArabicIsolatedFormPlugin' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/click/decorators.py:100): unused function 'pass_meta_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/gitdb/fun.py:93): unused function 'delta_duplicate' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/google/protobuf/internal/field_mask.py:47): unused method 'CanonicalFormFromMask' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/google/protobuf/internal/wire_format.py:45): unused variable 'FORMAT_FLOAT_LITTLE_ENDIAN' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/google/protobuf/internal/wire_format.py:46): unused variable 'FORMAT_DOUBLE_LITTLE_ENDIAN' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/google/protobuf/message.py:104): unused variable 'field_name_or_key' (100% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/httpx/_status_codes.py:97): unused variable 'NON_AUTHORITATIVE_INFORMATION' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/jinja2/compiler.py:1904): unused method 'visit_Keyword' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/jsonschema/_format.py:146): unused method 'conforms' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/jsonschema/tests/test_jsonschema_test_suite.py:220): unused variable 'TestDraft201909Format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/jsonschema/tests/test_jsonschema_test_suite.py:257): unused variable 'TestDraft202012Format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/mypy/fastparse.py:1632): unused method 'visit_FormattedValue' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/mypy/test/testinfer.py:14): unused class 'MapActualsToFormalsSuite' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/mypy/test/teststubgen.py:862): unused variable 'keyword_only' (100% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/mypy/test/teststubgen.py:862): unused variable 'keyword_only_with_default' (100% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/mypy/test/testtransform.py:14): unused class 'TransformSuite' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/mypyc/irbuild/specialize.py:621): unused function 'translate_str_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/narwhals/_arrow/group_by.py:61): unused attribute '_drop_null_keys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/narwhals/_pandas_like/group_by.py:47): unused attribute '_drop_null_keys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/numpy/_core/_exceptions.py:80): unused class '_UFuncInputCastingError' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/numpy/_core/_internal.py:874): unused function 'array_ufunc_errmsg_formatter' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/numpy/_core/_internal.py:886): unused function 'array_function_errmsg_formatter' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/numpy/_core/_internal.py:893): unused function '_ufunc_doc_signature_formatter' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/numpy/_utils/_inspect.py:168): unused function 'formatargvalues' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__init__.py:202): unused variable 'shared_lib_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/numpy/distutils/fcompiler/__init__.py:307): unused function 'verify_command_form' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/_types.py:172): unused variable '__key' (100% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/cli/_tools/migrate.py:64): unused variable 'KEYGEN_ACCOUNT' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/lib/streaming/responses/_responses.py:233): unused attribute '_rich_text_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/resources/beta/realtime/realtime.py:234): unused variable 'input_audio_buffer' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/resources/beta/realtime/realtime.py:246): unused attribute 'input_audio_buffer' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/resources/beta/realtime/realtime.py:416): unused variable 'input_audio_buffer' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/resources/beta/realtime/realtime.py:428): unused attribute 'input_audio_buffer' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/resources/responses/input_items.py:203): unused attribute '_input_items' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/resources/responses/input_items.py:212): unused attribute '_input_items' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/resources/responses/input_items.py:221): unused attribute '_input_items' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/resources/responses/input_items.py:230): unused attribute '_input_items' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/beta/realtime/realtime_response_usage.py:30): unused variable 'input_token_details' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/beta/realtime/realtime_response_usage.py:33): unused variable 'input_tokens' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/chat/chat_completion_content_part_input_audio_param.py:19): unused variable 'input_audio' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/evals/create_eval_completions_run_data_source.py:161): unused variable 'input_messages' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/evals/create_eval_completions_run_data_source_param.py:155): unused variable 'input_messages' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/evals/run_cancel_response.py:220): unused variable 'input_messages' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/evals/run_create_params.py:235): unused variable 'input_messages' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/evals/run_create_response.py:220): unused variable 'input_messages' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/evals/run_list_response.py:220): unused variable 'input_messages' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/evals/run_retrieve_response.py:220): unused variable 'input_messages' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/fine_tuning/alpha/grader_run_response.py:13): unused variable 'formula_parse_error' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/images_response.py:20): unused variable 'input_tokens' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/images_response.py:23): unused variable 'input_tokens_details' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/moderation.py:177): unused variable 'category_applied_input_types' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/responses/response_usage.py:22): unused variable 'input_tokens' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/openai/types/responses/response_usage.py:25): unused variable 'input_tokens_details' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/packaging/markers.py:65): unused variable 'platform_machine' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/packaging/markers.py:72): unused variable 'platform_release' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/packaging/markers.py:79): unused variable 'platform_system' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/packaging/markers.py:86): unused variable 'platform_version' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/packaging/markers.py:101): unused variable 'platform_python_implementation' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/packaging/markers.py:109): unused variable 'sys_platform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/packaging/metadata.py:94): unused variable 'supported_platforms' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/packaging/metadata.py:802): unused variable 'supported_platforms' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pandas/_version.py:150): unused function 'git_get_keywords' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pandas/io/excel/_openpyxl.py:405): unused method '_convert_to_number_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pandas/io/sas/sas_constants.py:22): unused variable 'platform_offset' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pandas/io/sas/sas_constants.py:23): unused variable 'platform_length' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pandas/tests/frame/methods/test_info.py:26): unused function 'duplicate_columns_frame' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pandas/tests/io/formats/test_eng_formatting.py:13): unused function 'reset_float_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/AvifImagePlugin.py:68): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/BlpImagePlugin.py:258): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/BmpImagePlugin.py:69): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/BmpImagePlugin.py:403): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/BufrStubImagePlugin.py:41): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/CurImagePlugin.py:38): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DcxImagePlugin.py:43): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:318): unused variable 'DXGI_FORMAT_R8G8B8A8_TYPELESS' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:319): unused variable 'DXGI_FORMAT_R8G8B8A8_UNORM' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:320): unused variable 'DXGI_FORMAT_R8G8B8A8_UNORM_SRGB' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:321): unused variable 'DXGI_FORMAT_BC5_TYPELESS' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:322): unused variable 'DXGI_FORMAT_BC5_UNORM' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:323): unused variable 'DXGI_FORMAT_BC5_SNORM' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:324): unused variable 'DXGI_FORMAT_BC6H_UF16' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:325): unused variable 'DXGI_FORMAT_BC6H_SF16' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:326): unused variable 'DXGI_FORMAT_BC7_TYPELESS' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:327): unused variable 'DXGI_FORMAT_BC7_UNORM' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:328): unused variable 'DXGI_FORMAT_BC7_UNORM_SRGB' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/DdsImagePlugin.py:333): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/EpsImagePlugin.py:187): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ExifTags.py:80): unused variable 'SampleFormat' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ExifTags.py:95): unused variable 'JpegPointTransforms' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ExifTags.py:104): unused variable 'RelatedImageFileFormat' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ExifTags.py:170): unused variable 'XPKeywords' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ExifTags.py:334): unused variable 'GPSAreaInformation' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ExifTags.py:347): unused variable 'RelatedImageFileFormat' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/FitsImagePlugin.py:25): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/FliImagePlugin.py:46): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/FpxImagePlugin.py:54): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/FtexImagePlugin.py:72): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/GbrImagePlugin.py:42): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/GdImageFile.py:47): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/GifImagePlugin.py:82): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/GribStubImagePlugin.py:41): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/Hdf5StubImagePlugin.py:41): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/IcnsImagePlugin.py:266): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/IcoImagePlugin.py:326): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/Image.py:540): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageCms.py:140): unused variable 'INPUT' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageCms.py:157): unused variable 'NULLTRANSFORM' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageCms.py:347): unused attribute 'inputMode' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageCms.py:720): unused variable 'buildTransformFromOpenProfiles' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageCms.py:721): unused variable 'buildProofTransformFromOpenProfiles' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageCms.py:724): unused function 'applyTransform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageDraw2.py:118): unused method 'settransform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageFile.py:248): unused method 'get_format_mimetype' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageOps.py:433): unused function 'deform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageTransform.py:46): unused class 'AffineTransform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageTransform.py:67): unused class 'PerspectiveTransform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageTransform.py:109): unused class 'QuadTransform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImageTransform.py:126): unused class 'MeshTransform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImImagePlugin.py:121): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/ImtImagePlugin.py:34): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/IptcImagePlugin.py:72): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/Jpeg2KImagePlugin.py:248): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/JpegImagePlugin.py:338): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/McIdasImagePlugin.py:35): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/MicImagePlugin.py:38): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/MpegImagePlugin.py:67): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/MpoImagePlugin.py:98): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/MspImagePlugin.py:50): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/PcdImagePlugin.py:28): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/PcxImagePlugin.py:51): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/PixarImagePlugin.py:40): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/PngImagePlugin.py:754): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/PpmImagePlugin.py:59): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/PsdImagePlugin.py:60): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/QoiImagePlugin.py:22): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/SgiImagePlugin.py:54): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/SpiderImagePlugin.py:101): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/SunImagePlugin.py:34): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/TgaImagePlugin.py:51): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/TiffImagePlugin.py:1162): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/WalImageFile.py:36): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/WebPImagePlugin.py:39): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/WmfImagePlugin.py:80): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/XbmImagePlugin.py:50): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/XpmImagePlugin.py:37): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/PIL/XVThumbImagePlugin.py:46): unused variable 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_internal/cli/parser.py:28): unused method 'format_option_strings' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_internal/cli/parser.py:57): unused method 'format_heading' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_internal/cli/parser.py:70): unused method 'format_description' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_internal/commands/search.py:25): unused class 'TransformedHit' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_internal/req/req_install.py:229): unused method 'format_debug' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/provider.py:24): unused variable 'PreferenceInformation' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_internal/utils/logging.py:74): unused variable 'default_time_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/colorama/tests/initialise_test.py:70): unused method 'testInitAutoresetOnWrapsOnAllPlatforms' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/distlib/compat.py:898): unused method 'viewkeys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/distlib/metadata.py:700): unused variable 'common_keys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/distlib/metadata.py:705): unused variable 'mapped_keys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/core.py:2292): unused method 'transformString' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/core.py:2594): unused variable 'setDefaultKeywordChars' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/pyparsing/exceptions.py:247): unused method 'markInputline' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/requests/auth.py:21): unused variable 'CONTENT_TYPE_FORM_URLENCODED' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/requests/utils.py:313): unused function 'from_key_val_list' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/six.py:610): unused variable 'viewkeys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/six.py:628): unused variable 'viewkeys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/typing_extensions.py:1064): unused attribute '__optional_keys__' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/typing_extensions.py:2434): unused attribute '__dataclass_transform__' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/bindings.py:451): unused variable 'kSecFormatPEMSequence' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/_securetransport/bindings.py:479): unused variable 'errSSLWeakPeerEphemeralDHKey' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/urllib3/contrib/securetransport.py:483): unused variable 'client_key_passphrase' (100% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/urllib3/fields.py:24): unused function 'format_header_param_rfc2231' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/urllib3/fields.py:123): unused variable 'format_header_param' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/six.py:651): unused variable 'viewkeys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pip/_vendor/urllib3/packages/six.py:670): unused variable 'viewkeys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/core.py:2207): unused variable 'transformString' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/core.py:2469): unused variable 'setDefaultKeywordChars' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/exceptions.py:217): unused variable 'markInputline' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pyarrow/acero.py:259): unused function '_perform_join_asof' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pyarrow/tests/parquet/encryption.py:32): unused method 'wrap_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pyarrow/tests/parquet/encryption.py:41): unused method 'unwrap_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pyarrow/tests/parquet/test_encryption.py:284): unused method 'wrap_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pyarrow/tests/parquet/test_encryption.py:287): unused method 'unwrap_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pyarrow/tests/parquet/test_encryption.py:338): unused method 'wrap_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pyarrow/tests/parquet/test_encryption.py:341): unused method 'unwrap_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pyarrow/tests/test_dataset_encryption.py:180): unused method 'wrap_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pyarrow/tests/test_dataset_encryption.py:184): unused method 'unwrap_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pydantic/_internal/_config.py:79): unused variable 'hide_input_in_errors' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pydantic/_internal/_core_metadata.py:43): unused variable 'pydantic_internal_union_tag_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pydantic/config.py:731): unused variable 'hide_input_in_errors' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pydantic/deprecated/decorator.py:272): unused method 'check_duplicate_kwargs' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pydantic/v1/decorator.py:252): unused function 'check_duplicate_kwargs' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pydantic_core/core_schema.py:109): unused variable 'hide_input_in_errors' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pydantic_core/core_schema.py:308): unused variable 'index_key' (100% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pydantic_core/core_schema.py:378): unused function 'format_ser_schema' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pydeck/widget/widget.py:57): unused variable 'carto_key' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pyflakes/checker.py:1760): unused variable 'FORMATTEDVALUE' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pygments/lexers/php.py:36): unused variable 'zephir_keywords' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/pylint/testutils/pyreverse.py:74): unused variable 'output_formats' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/requests/auth.py:21): unused variable 'CONTENT_TYPE_FORM_URLENCODED' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/requests/utils.py:318): unused function 'from_key_val_list' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/_msvccompiler.py:218): unused variable 'shared_lib_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/bcppcompiler.py:63): unused variable 'shared_lib_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/ccompiler.py:77): unused variable 'shared_lib_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/core.py:52): unused variable 'setup_keywords' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/core.py:77): unused variable 'extension_keywords' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/cygwinccompiler.py:77): unused variable 'shared_lib_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/dist.py:1228): unused method 'set_keywords' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/dist.py:1234): unused method 'set_platforms' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/msvc9compiler.py:347): unused variable 'shared_lib_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/msvccompiler.py:252): unused variable 'shared_lib_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/unixccompiler.py:141): unused variable 'shared_lib_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_distutils/unixccompiler.py:142): unused variable 'xcode_stub_lib_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/core.py:2207): unused variable 'transformString' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/core.py:2469): unused variable 'setDefaultKeywordChars' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_vendor/pyparsing/exceptions.py:217): unused variable 'markInputline' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/_vendor/typing_extensions.py:1085): unused attribute '__optional_keys__' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/fastjsonschema_validations.py:117): unused variable 'data__platforms_len' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/config/_validate_pyproject/fastjsonschema_validations.py:815): unused variable 'data__keywords_len' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/dist.py:916): unused method '_finalize_setup_keywords' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/setuptools/errors.py:22): unused variable 'PlatformError' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/six.py:615): unused variable 'viewkeys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/six.py:633): unused variable 'viewkeys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/config.py:473): unused function '_logger_message_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/delta_generator_singletons.py:93): unused property 'sidebar_dg' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/errors.py:152): unused class 'StreamlitModuleNotFoundError' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/external/langchain/streamlit_callback_handler.py:319): unused attribute '_max_thought_containers' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/logger.py:79): unused attribute 'default_msec_format' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Alert_pb2.py:15): unused import 'streamlit_dot_proto_dot_WidthConfig__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ArrowNamedDataSet_pb2.py:15): unused import 'streamlit_dot_proto_dot_Arrow__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ArrowVegaLiteChart_pb2.py:15): unused import 'streamlit_dot_proto_dot_Arrow__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ArrowVegaLiteChart_pb2.py:16): unused import 'streamlit_dot_proto_dot_ArrowNamedDataSet__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/AudioInput_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/BackMsg_pb2.py:15): unused import 'streamlit_dot_proto_dot_ClientState__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/BackMsg_pb2.py:16): unused import 'streamlit_dot_proto_dot_Common__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ButtonGroup_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/CameraInput_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Checkbox_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ClientState_pb2.py:15): unused import 'streamlit_dot_proto_dot_WidgetStates__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ColorPicker_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/DataFrame_pb2.py:15): unused import 'streamlit_dot_proto_dot_Common__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/DateInput_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Delta_pb2.py:15): unused import 'streamlit_dot_proto_dot_Block__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Delta_pb2.py:16): unused import 'streamlit_dot_proto_dot_Element__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Delta_pb2.py:17): unused import 'streamlit_dot_proto_dot_NamedDataSet__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Delta_pb2.py:18): unused import 'streamlit_dot_proto_dot_ArrowNamedDataSet__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:15): unused import 'streamlit_dot_proto_dot_Alert__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:16): unused import 'streamlit_dot_proto_dot_Arrow__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:17): unused import 'streamlit_dot_proto_dot_Audio__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:18): unused import 'streamlit_dot_proto_dot_AudioInput__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:19): unused import 'streamlit_dot_proto_dot_Balloons__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:20): unused import 'streamlit_dot_proto_dot_ArrowVegaLiteChart__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:21): unused import 'streamlit_dot_proto_dot_BokehChart__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:22): unused import 'streamlit_dot_proto_dot_Button__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:23): unused import 'streamlit_dot_proto_dot_ButtonGroup__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:24): unused import 'streamlit_dot_proto_dot_DownloadButton__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:25): unused import 'streamlit_dot_proto_dot_CameraInput__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:26): unused import 'streamlit_dot_proto_dot_ChatInput__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:27): unused import 'streamlit_dot_proto_dot_Checkbox__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:28): unused import 'streamlit_dot_proto_dot_Code__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:29): unused import 'streamlit_dot_proto_dot_ColorPicker__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:30): unused import 'streamlit_dot_proto_dot_DataFrame__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:31): unused import 'streamlit_dot_proto_dot_DateInput__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:32): unused import 'streamlit_dot_proto_dot_DeckGlJsonChart__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:33): unused import 'streamlit_dot_proto_dot_DocString__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:34): unused import 'streamlit_dot_proto_dot_Empty__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:35): unused import 'streamlit_dot_proto_dot_Exception__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:36): unused import 'streamlit_dot_proto_dot_Favicon__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:37): unused import 'streamlit_dot_proto_dot_FileUploader__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:38): unused import 'streamlit_dot_proto_dot_GraphVizChart__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:39): unused import 'streamlit_dot_proto_dot_Html__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:40): unused import 'streamlit_dot_proto_dot_IFrame__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:41): unused import 'streamlit_dot_proto_dot_Image__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:42): unused import 'streamlit_dot_proto_dot_Json__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:43): unused import 'streamlit_dot_proto_dot_LinkButton__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:44): unused import 'streamlit_dot_proto_dot_NumberInput__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:45): unused import 'streamlit_dot_proto_dot_Markdown__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:46): unused import 'streamlit_dot_proto_dot_Metric__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:47): unused import 'streamlit_dot_proto_dot_MultiSelect__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:48): unused import 'streamlit_dot_proto_dot_PageLink__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:49): unused import 'streamlit_dot_proto_dot_PlotlyChart__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:50): unused import 'streamlit_dot_proto_dot_Components__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:51): unused import 'streamlit_dot_proto_dot_Progress__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:52): unused import 'streamlit_dot_proto_dot_Snow__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:53): unused import 'streamlit_dot_proto_dot_Spinner__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:54): unused import 'streamlit_dot_proto_dot_Radio__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:55): unused import 'streamlit_dot_proto_dot_Selectbox__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:56): unused import 'streamlit_dot_proto_dot_Skeleton__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:57): unused import 'streamlit_dot_proto_dot_Slider__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:58): unused import 'streamlit_dot_proto_dot_Text__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:59): unused import 'streamlit_dot_proto_dot_TextArea__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:60): unused import 'streamlit_dot_proto_dot_TextInput__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:61): unused import 'streamlit_dot_proto_dot_TimeInput__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:62): unused import 'streamlit_dot_proto_dot_Toast__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:63): unused import 'streamlit_dot_proto_dot_VegaLiteChart__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:64): unused import 'streamlit_dot_proto_dot_Video__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Element_pb2.py:65): unused import 'streamlit_dot_proto_dot_Heading__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Exception_pb2.py:15): unused import 'streamlit_dot_proto_dot_WidthConfig__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/FileUploader_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:15): unused import 'streamlit_dot_proto_dot_AutoRerun__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:16): unused import 'streamlit_dot_proto_dot_Common__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:17): unused import 'streamlit_dot_proto_dot_Delta__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:18): unused import 'streamlit_dot_proto_dot_GitInfo__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:19): unused import 'streamlit_dot_proto_dot_Logo__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:20): unused import 'streamlit_dot_proto_dot_Navigation__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:21): unused import 'streamlit_dot_proto_dot_NewSession__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:22): unused import 'streamlit_dot_proto_dot_PageConfig__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:23): unused import 'streamlit_dot_proto_dot_PageInfo__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:24): unused import 'streamlit_dot_proto_dot_PageProfile__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:25): unused import 'streamlit_dot_proto_dot_PageNotFound__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:26): unused import 'streamlit_dot_proto_dot_PagesChanged__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:27): unused import 'streamlit_dot_proto_dot_ParentMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:28): unused import 'streamlit_dot_proto_dot_SessionEvent__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:29): unused import 'streamlit_dot_proto_dot_SessionStatus__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/ForwardMsg_pb2.py:30): unused import 'streamlit_dot_proto_dot_AuthRedirect__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Metric_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/MetricsEvent_pb2.py:15): unused import 'streamlit_dot_proto_dot_PageProfile__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/MultiSelect_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/NamedDataSet_pb2.py:15): unused import 'streamlit_dot_proto_dot_DataFrame__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Navigation_pb2.py:15): unused import 'streamlit_dot_proto_dot_AppPage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/NewSession_pb2.py:15): unused import 'streamlit_dot_proto_dot_AppPage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/NewSession_pb2.py:16): unused import 'streamlit_dot_proto_dot_SessionStatus__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/NumberInput_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/PagesChanged_pb2.py:15): unused import 'streamlit_dot_proto_dot_AppPage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Radio_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Selectbox_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/SessionEvent_pb2.py:15): unused import 'streamlit_dot_proto_dot_Exception__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/Slider_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/TextArea_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/TextInput_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/TimeInput_pb2.py:15): unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/VegaLiteChart_pb2.py:15): unused import 'streamlit_dot_proto_dot_DataFrame__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/VegaLiteChart_pb2.py:16): unused import 'streamlit_dot_proto_dot_NamedDataSet__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/WidgetStates_pb2.py:15): unused import 'streamlit_dot_proto_dot_Common__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/proto/WidgetStates_pb2.py:16): unused import 'streamlit_dot_proto_dot_Components__pb2' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/runtime/app_session.py:744): unused attribute 'streamlit_version' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/runtime/app_session.py:923): unused attribute 'hide_sidebar_nav' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/runtime/secrets.py:75): unused method 'set_missing_key_message' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/runtime/state/query_params_proxy.py:84): unused variable 'keys_and_values' (100% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/runtime/state/query_params_proxy.py:169): unused variable 'keys_and_values' (100% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/runtime/state/session_state.py:308): unused method 'set_key_id_mapping' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/streamlit/runtime/state/session_state.py:315): unused method 'get_key_from_id' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/tornado/gen.py:118): unused class 'KeyReuseError' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/tornado/gen.py:122): unused class 'UnknownKeyError' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/tornado/web.py:925): unused variable 'get_secure_cookie_key_version' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/tornado/web.py:2296): unused method 'add_transform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/tqdm/notebook.py:23): unused import 'ipywidgets' (90% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/tqdm/std.py:943): unused attribute 'progress_transform' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/typing_extensions.py:1090): unused attribute '__optional_keys__' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/typing_extensions.py:1091): unused attribute '__readonly_keys__' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/typing_extensions.py:1092): unused attribute '__mutable_keys__' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/typing_extensions.py:3073): unused attribute '__dataclass_transform__' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/_collections.py:15): unused class 'HasGettableStringKeys' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/fields.py:31): unused function 'format_header_param_rfc2231' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/fields.py:135): unused function 'format_header_param' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:64): unused variable 'key_scheme' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:65): unused variable 'key_host' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:66): unused variable 'key_port' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:67): unused variable 'key_timeout' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:68): unused variable 'key_retries' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:69): unused variable 'key_block' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:70): unused variable 'key_source_address' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:71): unused variable 'key_key_file' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:72): unused variable 'key_key_password' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:73): unused variable 'key_cert_file' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:74): unused variable 'key_cert_reqs' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:75): unused variable 'key_ca_certs' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:76): unused variable 'key_ca_cert_data' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:77): unused variable 'key_ssl_version' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:78): unused variable 'key_ssl_minimum_version' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:79): unused variable 'key_ssl_maximum_version' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:80): unused variable 'key_ca_cert_dir' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:81): unused variable 'key_ssl_context' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:82): unused variable 'key_maxsize' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:83): unused variable 'key_headers' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:84): unused variable 'key__proxy' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:85): unused variable 'key__proxy_headers' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:86): unused variable 'key__proxy_config' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:87): unused variable 'key_socket_options' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:88): unused variable 'key__socks_options' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:89): unused variable 'key_assert_hostname' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:90): unused variable 'key_assert_fingerprint' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:91): unused variable 'key_server_hostname' (60% confidence)
- **vulture** (.venv/lib/python3.11/site-packages/urllib3/poolmanager.py:92): unused variable 'key_blocksize' (60% confidence)

## Detailed Results
### pylint (🔥 Essential)
Detects misuse of widgets, naming issues, improper conditionals, repeated widget declarations

#### __init__.py
- Line 1: [parse-error] error while code parsing: Unable to load file __init__.py:
[Errno 2] No such file or directory: '__init__.py' (FATAL)

### mypy (✅ Very helpful)
Ensures Streamlit inputs (e.g. `st.date_input()`) are properly typed and used downstream

*No issues found.*

### bandit (✅ Important)
Warns about unsafe use of secrets, unsafe file I/O, and injection risks

*No issues found.*

### vulture (⚠️ Nice to have)
Finds unused UI elements or logic blocks (but may flag false positives due to Streamlit reactivity)

#### __init__.py
- Line 80: unused class '_TrivialRe' (60% confidence) (UNUSED)
- Line 99: unused method 'spec_for_distutils' (60% confidence) (UNUSED)
- Line 121: unused method 'create_module' (60% confidence) (UNUSED)
- Line 140: unused method 'spec_for_pip' (60% confidence) (UNUSED)
- Line 148: unused attribute 'spec_for_distutils' (60% confidence) (UNUSED)
- Line 176: unused attribute 'spec_for_distutils' (60% confidence) (UNUSED)
- Line 202: unused function 'add_shim' (60% confidence) (UNUSED)

#### __init__.py
- Line 30: unused property 'NaN' (60% confidence) (UNUSED)
- Line 35: unused property 'LN10' (60% confidence) (UNUSED)
- Line 45: unused property 'LOG10E' (60% confidence) (UNUSED)
- Line 50: unused property 'LOG2E' (60% confidence) (UNUSED)
- Line 55: unused property 'SQRT1_2' (60% confidence) (UNUSED)
- Line 60: unused property 'LN2' (60% confidence) (UNUSED)
- Line 65: unused property 'SQRT2' (60% confidence) (UNUSED)
- Line 70: unused property 'PI' (60% confidence) (UNUSED)
- Line 235: unused method 'isArray' (60% confidence) (UNUSED)
- Line 240: unused method 'isBoolean' (60% confidence) (UNUSED)
- Line 245: unused method 'isDate' (60% confidence) (UNUSED)
- Line 255: unused method 'isDefined' (60% confidence) (UNUSED)
- Line 264: unused method 'isNumber' (60% confidence) (UNUSED)
- Line 273: unused method 'isObject' (60% confidence) (UNUSED)
- Line 278: unused method 'isRegExp' (60% confidence) (UNUSED)
- Line 283: unused method 'isString' (60% confidence) (UNUSED)
- Line 288: unused method 'isValid' (60% confidence) (UNUSED)
- Line 293: unused method 'toBoolean' (60% confidence) (UNUSED)
- Line 302: unused method 'toDate' (60% confidence) (UNUSED)
- Line 313: unused method 'toNumber' (60% confidence) (UNUSED)
- Line 347: unused method 'isNaN' (60% confidence) (UNUSED)
- Line 359: unused method 'isFinite' (60% confidence) (UNUSED)
- Line 610: unused method 'sampleNormal' (60% confidence) (UNUSED)
- Line 624: unused method 'cumulativeNormal' (60% confidence) (UNUSED)
- Line 642: unused method 'densityNormal' (60% confidence) (UNUSED)
- Line 660: unused method 'quantileNormal' (60% confidence) (UNUSED)
- Line 678: unused method 'sampleLogNormal' (60% confidence) (UNUSED)
- Line 693: unused method 'cumulativeLogNormal' (60% confidence) (UNUSED)
- Line 712: unused method 'densityLogNormal' (60% confidence) (UNUSED)
- Line 731: unused method 'quantileLogNormal' (60% confidence) (UNUSED)
- Line 750: unused method 'sampleUniform' (60% confidence) (UNUSED)
- Line 765: unused method 'cumulativeUniform' (60% confidence) (UNUSED)
- Line 784: unused method 'densityUniform' (60% confidence) (UNUSED)
- Line 803: unused method 'quantileUniform' (60% confidence) (UNUSED)
- Line 914: unused method 'timezoneoffset' (60% confidence) (UNUSED)
- Line 919: unused method 'timeOffset' (60% confidence) (UNUSED)
- Line 934: unused method 'timeSequence' (60% confidence) (UNUSED)
- Line 978: unused method 'utcday' (60% confidence) (UNUSED)
- Line 983: unused method 'utcdayofyear' (60% confidence) (UNUSED)
- Line 988: unused method 'utcyear' (60% confidence) (UNUSED)
- Line 993: unused method 'utcquarter' (60% confidence) (UNUSED)
- Line 998: unused method 'utcmonth' (60% confidence) (UNUSED)
- Line 1003: unused method 'utcweek' (60% confidence) (UNUSED)
- Line 1014: unused method 'utchours' (60% confidence) (UNUSED)
- Line 1019: unused method 'utcminutes' (60% confidence) (UNUSED)
- Line 1024: unused method 'utcseconds' (60% confidence) (UNUSED)
- Line 1029: unused method 'utcmilliseconds' (60% confidence) (UNUSED)
- Line 1034: unused method 'utcOffset' (60% confidence) (UNUSED)
- Line 1049: unused method 'utcSequence' (60% confidence) (UNUSED)
- Line 1074: unused method 'clampRange' (60% confidence) (UNUSED)
- Line 1088: unused method 'indexof' (60% confidence) (UNUSED)
- Line 1093: unused method 'inrange' (60% confidence) (UNUSED)
- Line 1105: unused method 'lastindexof' (60% confidence) (UNUSED)
- Line 1115: unused method 'lerp' (60% confidence) (UNUSED)
- Line 1134: unused method 'pluck' (60% confidence) (UNUSED)
- Line 1206: unused method 'parseFloat' (60% confidence) (UNUSED)
- Line 1215: unused method 'parseInt' (60% confidence) (UNUSED)
- Line 1297: unused method 'dayFormat' (60% confidence) (UNUSED)
- Line 1306: unused method 'dayAbbrevFormat' (60% confidence) (UNUSED)
- Line 1328: unused method 'monthFormat' (60% confidence) (UNUSED)
- Line 1337: unused method 'monthAbbrevFormat' (60% confidence) (UNUSED)
- Line 1346: unused method 'timeUnitSpecifier' (60% confidence) (UNUSED)
- Line 1389: unused method 'timeParse' (60% confidence) (UNUSED)
- Line 1404: unused method 'utcFormat' (60% confidence) (UNUSED)
- Line 1424: unused method 'utcParse' (60% confidence) (UNUSED)
- Line 1483: unused method 'hsl' (60% confidence) (UNUSED)
- Line 1517: unused method 'hcl' (60% confidence) (UNUSED)
- Line 1534: unused method 'luminance' (60% confidence) (UNUSED)
- Line 1548: unused method 'contrast' (60% confidence) (UNUSED)
- Line 1610: unused method 'pinchDistance' (60% confidence) (UNUSED)
- Line 1615: unused method 'pinchAngle' (60% confidence) (UNUSED)
- Line 1620: unused method 'inScope' (60% confidence) (UNUSED)
- Line 1721: unused method 'bandspace' (60% confidence) (UNUSED)
- Line 1760: unused method 'panLinear' (60% confidence) (UNUSED)
- Line 1770: unused method 'panLog' (60% confidence) (UNUSED)
- Line 1780: unused method 'panPow' (60% confidence) (UNUSED)
- Line 1792: unused method 'panSymlog' (60% confidence) (UNUSED)
- Line 1804: unused method 'zoomLinear' (60% confidence) (UNUSED)
- Line 1820: unused method 'zoomLog' (60% confidence) (UNUSED)
- Line 1836: unused method 'zoomPow' (60% confidence) (UNUSED)
- Line 1853: unused method 'zoomSymlog' (60% confidence) (UNUSED)
- Line 1870: unused method 'geoArea' (60% confidence) (UNUSED)
- Line 1893: unused method 'geoBounds' (60% confidence) (UNUSED)
- Line 1919: unused method 'geoCentroid' (60% confidence) (UNUSED)
- Line 1942: unused method 'geoScale' (60% confidence) (UNUSED)
- Line 1954: unused method 'treePath' (60% confidence) (UNUSED)
- Line 1966: unused method 'treeAncestors' (60% confidence) (UNUSED)
- Line 1971: unused method 'containerSize' (60% confidence) (UNUSED)
- Line 1990: unused method 'windowSize' (60% confidence) (UNUSED)

#### consts.py
- Line 3: unused variable 'CONST_LISTING' (60% confidence) (UNUSED)

#### funcs.py
- Line 3: unused variable 'FUNCTION_LISTING' (60% confidence) (UNUSED)
- Line 167: unused variable 'NAME_MAP' (60% confidence) (UNUSED)

#### jupyter_chart.py
- Line 174: unused attribute '_esm' (60% confidence) (UNUSED)
- Line 177: unused attribute '_esm' (60% confidence) (UNUSED)
- Line 220: unused method '_on_change_chart' (60% confidence) (UNUSED)
- Line 234: unused attribute '_vl_selections' (60% confidence) (UNUSED)
- Line 315: unused attribute '_vl_selections' (60% confidence) (UNUSED)
- Line 325: unused attribute '_js_watch_plan' (60% confidence) (UNUSED)
- Line 343: unused attribute '_py_to_js_updates' (60% confidence) (UNUSED)
- Line 347: unused method '_on_change_params' (60% confidence) (UNUSED)
- Line 352: unused method '_on_change_selections' (60% confidence) (UNUSED)

#### _importers.py
- Line 108: unused function 'pyarrow_available' (60% confidence) (UNUSED)

#### _show.py
- Line 57: unused method 'do_GET' (60% confidence) (UNUSED)

#### data.py
- Line 67: unused variable 'TDataType' (60% confidence) (UNUSED)

#### display.py
- Line 53: unused method 'set_embed_options' (60% confidence) (UNUSED)

#### execeval.py
- Line 38: unused function 'eval_block' (60% confidence) (UNUSED)
- Line 46: unused function 'eval_block' (60% confidence) (UNUSED)
- Line 54: unused function 'eval_block' (60% confidence) (UNUSED)

#### schemapi.py
- Line 94: unused function 'enable_debug_mode' (60% confidence) (UNUSED)
- Line 99: unused function 'disable_debug_mode' (60% confidence) (UNUSED)
- Line 1595: unused attribute '__signature__' (60% confidence) (UNUSED)

#### server.py
- Line 35: unused class 'MockServer' (60% confidence) (UNUSED)
- Line 51: unused method 'do_GET' (60% confidence) (UNUSED)

#### api.py
- Line 2184: unused method 'open_editor' (60% confidence) (UNUSED)
- Line 2563: unused method 'transform_aggregate' (60% confidence) (UNUSED)
- Line 2641: unused method 'transform_bin' (60% confidence) (UNUSED)
- Line 2701: unused method 'transform_calculate' (60% confidence) (UNUSED)
- Line 2770: unused method 'transform_density' (60% confidence) (UNUSED)
- Line 2848: unused method 'transform_impute' (60% confidence) (UNUSED)
- Line 2918: unused method 'transform_joinaggregate' (60% confidence) (UNUSED)
- Line 2974: unused method 'transform_extent' (60% confidence) (UNUSED)
- Line 2995: unused method 'transform_filter' (60% confidence) (UNUSED)
- Line 3103: unused method 'transform_flatten' (60% confidence) (UNUSED)
- Line 3136: unused method 'transform_fold' (60% confidence) (UNUSED)
- Line 3164: unused method 'transform_loess' (60% confidence) (UNUSED)
- Line 3207: unused method 'transform_lookup' (60% confidence) (UNUSED)
- Line 3261: unused method 'transform_pivot' (60% confidence) (UNUSED)
- Line 3308: unused method 'transform_quantile' (60% confidence) (UNUSED)
- Line 3355: unused method 'transform_regression' (60% confidence) (UNUSED)
- Line 3423: unused method 'transform_sample' (60% confidence) (UNUSED)
- Line 3443: unused method 'transform_stack' (60% confidence) (UNUSED)
- Line 3485: unused method 'transform_timeunit' (60% confidence) (UNUSED)
- Line 3568: unused method 'transform_window' (60% confidence) (UNUSED)
- Line 3783: unused method 'resolve_axis' (60% confidence) (UNUSED)
- Line 3789: unused method 'resolve_legend' (60% confidence) (UNUSED)
- Line 3795: unused method 'resolve_scale' (60% confidence) (UNUSED)
- Line 4072: unused method 'add_selection' (60% confidence) (UNUSED)
- Line 4288: unused method 'add_selection' (60% confidence) (UNUSED)
- Line 4412: unused method 'add_selection' (60% confidence) (UNUSED)
- Line 4516: unused method 'add_selection' (60% confidence) (UNUSED)
- Line 4622: unused method 'add_selection' (60% confidence) (UNUSED)
- Line 4703: unused method 'add_layers' (60% confidence) (UNUSED)
- Line 4748: unused method 'add_selection' (60% confidence) (UNUSED)
- Line 4842: unused method 'add_selection' (60% confidence) (UNUSED)

#### mixins.py
- Line 990: unused method 'mark_arc' (60% confidence) (UNUSED)
- Line 1010: unused method 'mark_bar' (60% confidence) (UNUSED)
- Line 1020: unused method 'mark_image' (60% confidence) (UNUSED)
- Line 1030: unused method 'mark_line' (60% confidence) (UNUSED)
- Line 1050: unused method 'mark_rect' (60% confidence) (UNUSED)
- Line 1060: unused method 'mark_rule' (60% confidence) (UNUSED)
- Line 1070: unused method 'mark_text' (60% confidence) (UNUSED)
- Line 1080: unused method 'mark_tick' (60% confidence) (UNUSED)
- Line 1090: unused method 'mark_trail' (60% confidence) (UNUSED)
- Line 1100: unused method 'mark_circle' (60% confidence) (UNUSED)
- Line 1110: unused method 'mark_square' (60% confidence) (UNUSED)
- Line 1120: unused method 'mark_geoshape' (60% confidence) (UNUSED)
- Line 1130: unused method 'mark_boxplot' (60% confidence) (UNUSED)
- Line 1140: unused method 'mark_errorbar' (60% confidence) (UNUSED)
- Line 1150: unused method 'mark_errorband' (60% confidence) (UNUSED)
- Line 1170: unused method 'configure_arc' (60% confidence) (UNUSED)
- Line 1178: unused method 'configure_area' (60% confidence) (UNUSED)
- Line 1186: unused method 'configure_axis' (60% confidence) (UNUSED)
- Line 1194: unused method 'configure_axisBand' (60% confidence) (UNUSED)
- Line 1202: unused method 'configure_axisBottom' (60% confidence) (UNUSED)
- Line 1210: unused method 'configure_axisDiscrete' (60% confidence) (UNUSED)
- Line 1218: unused method 'configure_axisLeft' (60% confidence) (UNUSED)
- Line 1226: unused method 'configure_axisPoint' (60% confidence) (UNUSED)
- Line 1234: unused method 'configure_axisQuantitative' (60% confidence) (UNUSED)
- Line 1242: unused method 'configure_axisRight' (60% confidence) (UNUSED)
- Line 1250: unused method 'configure_axisTemporal' (60% confidence) (UNUSED)
- Line 1258: unused method 'configure_axisTop' (60% confidence) (UNUSED)
- Line 1266: unused method 'configure_axisX' (60% confidence) (UNUSED)
- Line 1274: unused method 'configure_axisXBand' (60% confidence) (UNUSED)
- Line 1282: unused method 'configure_axisXDiscrete' (60% confidence) (UNUSED)
- Line 1290: unused method 'configure_axisXPoint' (60% confidence) (UNUSED)
- Line 1298: unused method 'configure_axisXQuantitative' (60% confidence) (UNUSED)
- Line 1306: unused method 'configure_axisXTemporal' (60% confidence) (UNUSED)
- Line 1314: unused method 'configure_axisY' (60% confidence) (UNUSED)
- Line 1322: unused method 'configure_axisYBand' (60% confidence) (UNUSED)
- Line 1330: unused method 'configure_axisYDiscrete' (60% confidence) (UNUSED)
- Line 1338: unused method 'configure_axisYPoint' (60% confidence) (UNUSED)
- Line 1346: unused method 'configure_axisYQuantitative' (60% confidence) (UNUSED)
- Line 1354: unused method 'configure_axisYTemporal' (60% confidence) (UNUSED)
- Line 1362: unused method 'configure_bar' (60% confidence) (UNUSED)
- Line 1370: unused method 'configure_boxplot' (60% confidence) (UNUSED)
- Line 1378: unused method 'configure_circle' (60% confidence) (UNUSED)
- Line 1386: unused method 'configure_concat' (60% confidence) (UNUSED)
- Line 1394: unused method 'configure_errorband' (60% confidence) (UNUSED)
- Line 1402: unused method 'configure_errorbar' (60% confidence) (UNUSED)
- Line 1410: unused method 'configure_facet' (60% confidence) (UNUSED)
- Line 1418: unused method 'configure_geoshape' (60% confidence) (UNUSED)
- Line 1426: unused method 'configure_header' (60% confidence) (UNUSED)
- Line 1434: unused method 'configure_headerColumn' (60% confidence) (UNUSED)
- Line 1442: unused method 'configure_headerFacet' (60% confidence) (UNUSED)
- Line 1450: unused method 'configure_headerRow' (60% confidence) (UNUSED)
- Line 1458: unused method 'configure_image' (60% confidence) (UNUSED)
- Line 1474: unused method 'configure_line' (60% confidence) (UNUSED)
- Line 1482: unused method 'configure_mark' (60% confidence) (UNUSED)
- Line 1490: unused method 'configure_point' (60% confidence) (UNUSED)
- Line 1498: unused method 'configure_projection' (60% confidence) (UNUSED)
- Line 1506: unused method 'configure_range' (60% confidence) (UNUSED)
- Line 1514: unused method 'configure_rect' (60% confidence) (UNUSED)
- Line 1522: unused method 'configure_rule' (60% confidence) (UNUSED)
- Line 1530: unused method 'configure_scale' (60% confidence) (UNUSED)
- Line 1538: unused method 'configure_selection' (60% confidence) (UNUSED)
- Line 1546: unused method 'configure_square' (60% confidence) (UNUSED)
- Line 1554: unused method 'configure_text' (60% confidence) (UNUSED)
- Line 1562: unused method 'configure_tick' (60% confidence) (UNUSED)
- Line 1570: unused method 'configure_title' (60% confidence) (UNUSED)
- Line 1578: unused method 'configure_tooltipFormat' (60% confidence) (UNUSED)
- Line 1586: unused method 'configure_trail' (60% confidence) (UNUSED)
- Line 1594: unused method 'configure_view' (60% confidence) (UNUSED)

#### __init__.py
- Line 69: unused variable '__other' (100% confidence) (UNUSED)
- Line 74: unused variable '__other' (100% confidence) (UNUSED)
- Line 79: unused variable '__other' (100% confidence) (UNUSED)
- Line 84: unused variable '__other' (100% confidence) (UNUSED)
- Line 89: unused variable '__other' (100% confidence) (UNUSED)
- Line 94: unused variable '__other' (100% confidence) (UNUSED)
- Line 184: unused property '__is_annotated_types_grouped_metadata__' (60% confidence) (UNUSED)

#### _asyncio.py
- Line 291: unused attribute '_executor_shutdown_called' (60% confidence) (UNUSED)
- Line 1171: unused method 'connection_made' (60% confidence) (UNUSED)
- Line 1178: unused method 'connection_lost' (60% confidence) (UNUSED)
- Line 1191: unused method 'eof_received' (60% confidence) (UNUSED)
- Line 1196: unused method 'pause_writing' (60% confidence) (UNUSED)
- Line 1199: unused method 'resume_writing' (60% confidence) (UNUSED)
- Line 1209: unused method 'connection_made' (60% confidence) (UNUSED)
- Line 1215: unused method 'connection_lost' (60% confidence) (UNUSED)
- Line 1219: unused method 'datagram_received' (60% confidence) (UNUSED)
- Line 1224: unused method 'error_received' (60% confidence) (UNUSED)
- Line 1227: unused method 'pause_writing' (60% confidence) (UNUSED)
- Line 1230: unused method 'resume_writing' (60% confidence) (UNUSED)
- Line 1408: unused method 'receive_fds' (60% confidence) (UNUSED)
- Line 1447: unused method 'send_fds' (60% confidence) (UNUSED)

#### _trio.py
- Line 356: unused class '_ProcessPoolShutdownInstrument' (60% confidence) (UNUSED)
- Line 361: unused variable 'current_default_worker_process_limiter' (60% confidence) (UNUSED)
- Line 449: unused method 'receive_fds' (60% confidence) (UNUSED)
- Line 482: unused method 'send_fds' (60% confidence) (UNUSED)

#### _fileio.py
- Line 493: unused method 'hardlink_to' (60% confidence) (UNUSED)
- Line 533: unused method 'is_mount' (60% confidence) (UNUSED)
- Line 713: unused method 'with_stem' (60% confidence) (UNUSED)
- Line 719: unused method 'with_segments' (60% confidence) (UNUSED)

#### _sockets.py
- Line 52: unused variable 'IPAddressFamily' (60% confidence) (UNUSED)
- Line 726: unused variable 'flowinfo' (60% confidence) (UNUSED)

#### _synchronization.py
- Line 67: unused variable 'lock_statistics' (60% confidence) (UNUSED)

#### _sockets.py
- Line 29: unused class '_NullAsyncContextManager' (60% confidence) (UNUSED)
- Line 104: unused method 'send_fds' (60% confidence) (UNUSED)
- Line 114: unused method 'receive_fds' (60% confidence) (UNUSED)

#### from_thread.py
- Line 380: unused method 'wrap_async_context_manager' (60% confidence) (UNUSED)
- Line 398: unused class 'BlockingPortalProvider' (60% confidence) (UNUSED)

#### pytest_plugin.py
- Line 67: unused function 'pytest_configure' (60% confidence) (UNUSED)
- Line 74: unused function 'pytest_fixture_setup' (60% confidence) (UNUSED)
- Line 125: unused function 'pytest_pycollect_makeitem' (60% confidence) (UNUSED)
- Line 136: unused function 'pytest_pyfunc_call' (60% confidence) (UNUSED)
- Line 178: unused function 'anyio_backend_name' (60% confidence) (UNUSED)
- Line 186: unused function 'anyio_backend_options' (60% confidence) (UNUSED)
- Line 265: unused function 'free_tcp_port' (60% confidence) (UNUSED)
- Line 270: unused function 'free_udp_port' (60% confidence) (UNUSED)

#### memory.py
- Line 25: unused variable 'current_buffer_used' (60% confidence) (UNUSED)
- Line 28: unused variable 'open_send_streams' (60% confidence) (UNUSED)
- Line 29: unused variable 'open_receive_streams' (60% confidence) (UNUSED)
- Line 31: unused variable 'tasks_waiting_send' (60% confidence) (UNUSED)
- Line 33: unused variable 'tasks_waiting_receive' (60% confidence) (UNUSED)

#### stapled.py
- Line 22: unused class 'StapledByteStream' (60% confidence) (UNUSED)
- Line 58: unused class 'StapledObjectStream' (60% confidence) (UNUSED)

#### text.py
- Line 96: unused class 'TextStream' (60% confidence) (UNUSED)

#### tls.py
- Line 266: unused class 'TLSListener' (60% confidence) (UNUSED)

#### brain_functools.py
- Line 34: unused property 'attr___wrapped__' (60% confidence) (UNUSED)
- Line 38: unused property 'attr_cache_info' (60% confidence) (UNUSED)
- Line 59: unused property 'attr_cache_clear' (60% confidence) (UNUSED)

#### const.py
- Line 13: unused variable 'WIN32' (60% confidence) (UNUSED)

#### decorators.py
- Line 109: unused function 'deprecate_default_argument_values' (60% confidence) (UNUSED)
- Line 172: unused function 'deprecate_arguments' (60% confidence) (UNUSED)
- Line 212: unused function 'deprecate_default_argument_values' (60% confidence) (UNUSED)
- Line 225: unused function 'deprecate_arguments' (60% confidence) (UNUSED)

#### spec.py
- Line 46: unused variable 'PY_CODERESOURCE' (60% confidence) (UNUSED)
- Line 49: unused variable 'PY_RESOURCE' (60% confidence) (UNUSED)

#### objectmodel.py
- Line 135: unused property 'attr___new__' (60% confidence) (UNUSED)
- Line 149: unused property 'attr___init__' (60% confidence) (UNUSED)
- Line 172: unused property 'attr_builtins' (60% confidence) (UNUSED)
- Line 176: unused property 'attr___path__' (60% confidence) (UNUSED)
- Line 196: unused property 'attr___name__' (60% confidence) (UNUSED)
- Line 200: unused property 'attr___doc__' (60% confidence) (UNUSED)
- Line 207: unused property 'attr___file__' (60% confidence) (UNUSED)
- Line 215: unused property 'attr___package__' (60% confidence) (UNUSED)
- Line 228: unused property 'attr___spec__' (60% confidence) (UNUSED)
- Line 233: unused property 'attr___loader__' (60% confidence) (UNUSED)
- Line 238: unused property 'attr___cached__' (60% confidence) (UNUSED)
- Line 245: unused property 'attr___name__' (60% confidence) (UNUSED)
- Line 249: unused property 'attr___doc__' (60% confidence) (UNUSED)
- Line 260: unused property 'attr___defaults__' (60% confidence) (UNUSED)
- Line 320: unused variable 'attr___globals__' (60% confidence) (UNUSED)
- Line 322: unused property 'attr___kwdefaults__' (60% confidence) (UNUSED)
- Line 351: unused property 'attr___get__' (60% confidence) (UNUSED)
- Line 467: unused variable 'attr___subclasshook__' (60% confidence) (UNUSED)
- Line 468: unused variable 'attr___str__' (60% confidence) (UNUSED)
- Line 469: unused variable 'attr___sizeof__' (60% confidence) (UNUSED)
- Line 470: unused variable 'attr___setattr___' (60% confidence) (UNUSED)
- Line 471: unused variable 'attr___repr__' (60% confidence) (UNUSED)
- Line 472: unused variable 'attr___reduce__' (60% confidence) (UNUSED)
- Line 473: unused variable 'attr___reduce_ex__' (60% confidence) (UNUSED)
- Line 474: unused variable 'attr___lt__' (60% confidence) (UNUSED)
- Line 475: unused variable 'attr___eq__' (60% confidence) (UNUSED)
- Line 476: unused variable 'attr___gt__' (60% confidence) (UNUSED)
- Line 477: unused variable 'attr___format__' (60% confidence) (UNUSED)
- Line 478: unused variable 'attr___delattr___' (60% confidence) (UNUSED)
- Line 479: unused variable 'attr___getattribute__' (60% confidence) (UNUSED)
- Line 480: unused variable 'attr___hash__' (60% confidence) (UNUSED)
- Line 481: unused variable 'attr___dir__' (60% confidence) (UNUSED)
- Line 482: unused variable 'attr___call__' (60% confidence) (UNUSED)
- Line 484: unused variable 'attr___closure__' (60% confidence) (UNUSED)
- Line 485: unused variable 'attr___code__' (60% confidence) (UNUSED)
- Line 503: unused property 'attr___name__' (60% confidence) (UNUSED)
- Line 511: unused property 'attr___doc__' (60% confidence) (UNUSED)
- Line 525: unused property 'attr_mro' (60% confidence) (UNUSED)
- Line 546: unused property 'attr___bases__' (60% confidence) (UNUSED)
- Line 561: unused property 'attr___subclasses__' (60% confidence) (UNUSED)
- Line 606: unused property 'attr___call__' (60% confidence) (UNUSED)
- Line 613: unused property 'attr___thisclass__' (60% confidence) (UNUSED)
- Line 617: unused property 'attr___self_class__' (60% confidence) (UNUSED)
- Line 646: unused variable 'attr_im_func' (60% confidence) (UNUSED)
- Line 647: unused variable 'attr_im_class' (60% confidence) (UNUSED)
- Line 648: unused variable 'attr_im_self' (60% confidence) (UNUSED)
- Line 658: unused property 'attr___enter__' (60% confidence) (UNUSED)
- Line 676: unused property 'attr___exit__' (60% confidence) (UNUSED)
- Line 722: unused property 'attr___name__' (60% confidence) (UNUSED)
- Line 728: unused property 'attr___doc__' (60% confidence) (UNUSED)
- Line 736: unused class 'AsyncGeneratorModel' (60% confidence) (UNUSED)
- Line 766: unused property 'attr___doc__' (60% confidence) (UNUSED)
- Line 779: unused property 'attr_args' (60% confidence) (UNUSED)
- Line 783: unused property 'attr___traceback__' (60% confidence) (UNUSED)
- Line 791: unused property 'attr_text' (60% confidence) (UNUSED)
- Line 801: unused property 'attr_errno' (60% confidence) (UNUSED)
- Line 805: unused property 'attr_strerror' (60% confidence) (UNUSED)
- Line 809: unused variable 'attr_filename2' (60% confidence) (UNUSED)
- Line 817: unused property 'attr_path' (60% confidence) (UNUSED)
- Line 823: unused property 'attr_object' (60% confidence) (UNUSED)
- Line 871: unused property 'attr_items' (60% confidence) (UNUSED)
- Line 886: unused property 'attr_keys' (60% confidence) (UNUSED)
- Line 937: unused property 'attr_fget' (60% confidence) (UNUSED)
- Line 968: unused property 'attr_fset' (60% confidence) (UNUSED)
- Line 1017: unused property 'attr_setter' (60% confidence) (UNUSED)
- Line 1021: unused property 'attr_deleter' (60% confidence) (UNUSED)
- Line 1025: unused property 'attr_getter' (60% confidence) (UNUSED)

#### manager.py
- Line 171: unused method 'ast_from_string' (60% confidence) (UNUSED)
- Line 358: unused method 'ast_from_class' (60% confidence) (UNUSED)

#### modutils.py
- Line 48: unused variable 'PY_COMPILED_EXTS' (60% confidence) (UNUSED)
- Line 52: unused variable 'PY_COMPILED_EXTS' (60% confidence) (UNUSED)
- Line 544: unused function 'is_standard_module' (60% confidence) (UNUSED)

#### as_string.py
- Line 99: unused method 'visit_await' (60% confidence) (UNUSED)
- Line 102: unused method 'visit_asyncwith' (60% confidence) (UNUSED)
- Line 105: unused method 'visit_asyncfor' (60% confidence) (UNUSED)
- Line 112: unused method 'visit_assignattr' (60% confidence) (UNUSED)
- Line 116: unused method 'visit_assert' (60% confidence) (UNUSED)
- Line 131: unused method 'visit_augassign' (60% confidence) (UNUSED)
- Line 135: unused method 'visit_annassign' (60% confidence) (UNUSED)
- Line 144: unused method 'visit_binop' (60% confidence) (UNUSED)
- Line 153: unused method 'visit_boolop' (60% confidence) (UNUSED)
- Line 158: unused method 'visit_break' (60% confidence) (UNUSED)
- Line 188: unused method 'visit_compare' (60% confidence) (UNUSED)
- Line 202: unused method 'visit_const' (60% confidence) (UNUSED)
- Line 208: unused method 'visit_continue' (60% confidence) (UNUSED)
- Line 212: unused method 'visit_delete' (60% confidence) (UNUSED)
- Line 216: unused method 'visit_delattr' (60% confidence) (UNUSED)
- Line 220: unused method 'visit_delname' (60% confidence) (UNUSED)
- Line 228: unused method 'visit_dict' (60% confidence) (UNUSED)
- Line 242: unused method 'visit_dictunpack' (60% confidence) (UNUSED)
- Line 245: unused method 'visit_dictcomp' (60% confidence) (UNUSED)
- Line 253: unused method 'visit_expr' (60% confidence) (UNUSED)
- Line 257: unused method 'visit_emptynode' (60% confidence) (UNUSED)
- Line 261: unused method 'visit_excepthandler' (60% confidence) (UNUSED)
- Line 274: unused method 'visit_empty' (60% confidence) (UNUSED)
- Line 287: unused method 'visit_importfrom' (60% confidence) (UNUSED)
- Line 293: unused method 'visit_joinedstr' (60% confidence) (UNUSED)
- Line 320: unused method 'visit_formattedvalue' (60% confidence) (UNUSED)
- Line 355: unused method 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 359: unused method 'visit_generatorexp' (60% confidence) (UNUSED)
- Line 380: unused method 'visit_global' (60% confidence) (UNUSED)
- Line 384: unused method 'visit_if' (60% confidence) (UNUSED)
- Line 393: unused method 'visit_ifexp' (60% confidence) (UNUSED)
- Line 411: unused method 'visit_lambda' (60% confidence) (UNUSED)
- Line 420: unused method 'visit_list' (60% confidence) (UNUSED)
- Line 424: unused method 'visit_listcomp' (60% confidence) (UNUSED)
- Line 439: unused method 'visit_namedexpr' (60% confidence) (UNUSED)
- Line 445: unused method 'visit_nonlocal' (60% confidence) (UNUSED)
- Line 449: unused method 'visit_paramspec' (60% confidence) (UNUSED)
- Line 453: unused method 'visit_pass' (60% confidence) (UNUSED)
- Line 457: unused method 'visit_partialfunction' (60% confidence) (UNUSED)
- Line 461: unused method 'visit_raise' (60% confidence) (UNUSED)
- Line 480: unused method 'visit_set' (60% confidence) (UNUSED)
- Line 484: unused method 'visit_setcomp' (60% confidence) (UNUSED)
- Line 490: unused method 'visit_slice' (60% confidence) (UNUSED)
- Line 499: unused method 'visit_subscript' (60% confidence) (UNUSED)
- Line 522: unused method 'visit_trystar' (60% confidence) (UNUSED)
- Line 533: unused method 'visit_tuple' (60% confidence) (UNUSED)
- Line 539: unused method 'visit_typealias' (60% confidence) (UNUSED)
- Line 543: unused method 'visit_typevar' (60% confidence) (UNUSED)
- Line 547: unused method 'visit_typevartuple' (60% confidence) (UNUSED)
- Line 551: unused method 'visit_unaryop' (60% confidence) (UNUSED)
- Line 583: unused method 'visit_yieldfrom' (60% confidence) (UNUSED)
- Line 592: unused method 'visit_starred' (60% confidence) (UNUSED)
- Line 596: unused method 'visit_match' (60% confidence) (UNUSED)
- Line 600: unused method 'visit_matchcase' (60% confidence) (UNUSED)
- Line 608: unused method 'visit_matchvalue' (60% confidence) (UNUSED)
- Line 612: unused method 'visit_matchsingleton' (60% confidence) (UNUSED)
- Line 617: unused method 'visit_matchsequence' (60% confidence) (UNUSED)
- Line 623: unused method 'visit_matchmapping' (60% confidence) (UNUSED)
- Line 635: unused method 'visit_matchclass' (60% confidence) (UNUSED)
- Line 647: unused method 'visit_matchstar' (60% confidence) (UNUSED)
- Line 651: unused method 'visit_matchas' (60% confidence) (UNUSED)
- Line 664: unused method 'visit_matchor' (60% confidence) (UNUSED)
- Line 672: unused method 'visit_frozenset' (60% confidence) (UNUSED)
- Line 675: unused method 'visit_super' (60% confidence) (UNUSED)
- Line 681: unused method 'visit_property' (60% confidence) (UNUSED)
- Line 684: unused method 'visit_evaluatedobject' (60% confidence) (UNUSED)
- Line 687: unused method 'visit_unknown' (60% confidence) (UNUSED)
- Line 703: unused variable 'to_code' (60% confidence) (UNUSED)

#### node_classes.py
- Line 74: unused variable 'AssignedStmtsCall' (60% confidence) (UNUSED)
- Line 83: unused variable 'InferBinaryOperation' (60% confidence) (UNUSED)
- Line 87: unused variable 'InferLHS' (60% confidence) (UNUSED)
- Line 91: unused variable 'InferUnaryOp' (60% confidence) (UNUSED)

#### node_ng.py
- Line 621: unused method 'repr_tree' (60% confidence) (UNUSED)
- Line 672: unused function '_repr_seq' (60% confidence) (UNUSED)
- Line 705: unused function '_repr_node' (60% confidence) (UNUSED)

#### scoped_nodes.py
- Line 524: unused method 'wildcard_import_names' (60% confidence) (UNUSED)

#### protocols.py
- Line 885: unreachable code after 'return' (100% confidence) (UNUSED)
- Line 899: unreachable code after 'return' (100% confidence) (UNUSED)

#### raw_building.py
- Line 232: unused function 'build_from_import' (60% confidence) (UNUSED)

#### rebuilder.py
- Line 48: unused variable 'NodesWithDocsType' (60% confidence) (UNUSED)
- Line 554: unused method 'visit_assert' (60% confidence) (UNUSED)
- Line 625: unused method 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 630: unused method 'visit_asyncfor' (60% confidence) (UNUSED)
- Line 633: unused method 'visit_await' (60% confidence) (UNUSED)
- Line 644: unused method 'visit_asyncwith' (60% confidence) (UNUSED)
- Line 664: unused method 'visit_annassign' (60% confidence) (UNUSED)
- Line 711: unused method 'visit_augassign' (60% confidence) (UNUSED)
- Line 726: unused method 'visit_binop' (60% confidence) (UNUSED)
- Line 741: unused method 'visit_boolop' (60% confidence) (UNUSED)
- Line 754: unused method 'visit_break' (60% confidence) (UNUSED)
- Line 820: unused method 'visit_continue' (60% confidence) (UNUSED)
- Line 830: unused method 'visit_compare' (60% confidence) (UNUSED)
- Line 901: unused method 'visit_delete' (60% confidence) (UNUSED)
- Line 932: unused method 'visit_dict' (60% confidence) (UNUSED)
- Line 947: unused method 'visit_dictcomp' (60% confidence) (UNUSED)
- Line 963: unused method 'visit_expr' (60% confidence) (UNUSED)
- Line 975: unused method 'visit_excepthandler' (60% confidence) (UNUSED)
- Line 1027: unused method 'visit_importfrom' (60% confidence) (UNUSED)
- Line 1122: unused method 'visit_generatorexp' (60% confidence) (UNUSED)
- Line 1183: unused method 'visit_global' (60% confidence) (UNUSED)
- Line 1198: unused method 'visit_if' (60% confidence) (UNUSED)
- Line 1214: unused method 'visit_ifexp' (60% confidence) (UNUSED)
- Line 1247: unused method 'visit_joinedstr' (60% confidence) (UNUSED)
- Line 1258: unused method 'visit_formattedvalue' (60% confidence) (UNUSED)
- Line 1275: unused method 'visit_namedexpr' (60% confidence) (UNUSED)
- Line 1302: unused method 'visit_lambda' (60% confidence) (UNUSED)
- Line 1314: unused method 'visit_list' (60% confidence) (UNUSED)
- Line 1328: unused method 'visit_listcomp' (60% confidence) (UNUSED)
- Line 1382: unused method 'visit_nonlocal' (60% confidence) (UNUSED)
- Line 1393: unused method 'visit_constant' (60% confidence) (UNUSED)
- Line 1405: unused method 'visit_paramspec' (60% confidence) (UNUSED)
- Line 1419: unused method 'visit_pass' (60% confidence) (UNUSED)
- Line 1429: unused method 'visit_raise' (60% confidence) (UNUSED)
- Line 1457: unused method 'visit_set' (60% confidence) (UNUSED)
- Line 1469: unused method 'visit_setcomp' (60% confidence) (UNUSED)
- Line 1484: unused method 'visit_slice' (60% confidence) (UNUSED)
- Line 1501: unused method 'visit_subscript' (60% confidence) (UNUSED)
- Line 1517: unused method 'visit_starred' (60% confidence) (UNUSED)
- Line 1548: unused method 'visit_trystar' (60% confidence) (UNUSED)
- Line 1564: unused method 'visit_tuple' (60% confidence) (UNUSED)
- Line 1578: unused method 'visit_typealias' (60% confidence) (UNUSED)
- Line 1594: unused method 'visit_typevar' (60% confidence) (UNUSED)
- Line 1611: unused method 'visit_typevartuple' (60% confidence) (UNUSED)
- Line 1627: unused method 'visit_unaryop' (60% confidence) (UNUSED)
- Line 1708: unused method 'visit_yieldfrom' (60% confidence) (UNUSED)
- Line 1721: unused method 'visit_match' (60% confidence) (UNUSED)
- Line 1735: unused method 'visit_matchcase' (60% confidence) (UNUSED)
- Line 1746: unused method 'visit_matchvalue' (60% confidence) (UNUSED)
- Line 1759: unused method 'visit_matchsingleton' (60% confidence) (UNUSED)
- Line 1771: unused method 'visit_matchsequence' (60% confidence) (UNUSED)
- Line 1786: unused method 'visit_matchmapping' (60% confidence) (UNUSED)
- Line 1805: unused method 'visit_matchclass' (60% confidence) (UNUSED)
- Line 1825: unused method 'visit_matchstar' (60% confidence) (UNUSED)
- Line 1840: unused method 'visit_matchas' (60% confidence) (UNUSED)
- Line 1856: unused method 'visit_matchor' (60% confidence) (UNUSED)

#### test_utils.py
- Line 52: unused function 'get_name_node' (60% confidence) (UNUSED)
- Line 56: unused function 'enable_warning' (60% confidence) (UNUSED)
- Line 67: unused function 'brainless_manager' (60% confidence) (UNUSED)

#### _compat.py
- Line 16: unused variable 'PY_3_12_PLUS' (60% confidence) (UNUSED)
- Line 87: unused variable 'repr_context' (60% confidence) (UNUSED)

#### _make.py
- Line 89: unused class '_CacheHashWrapper' (60% confidence) (UNUSED)
- Line 287: unused variable 'base_attrs_map' (60% confidence) (UNUSED)

#### exceptions.py
- Line 72: unused class 'PythonTooOldError' (60% confidence) (UNUSED)

#### calls.py
- Line 343: unused function 'gen_blacklist' (60% confidence) (UNUSED)

#### imports.py
- Line 234: unused function 'gen_blacklist' (60% confidence) (UNUSED)

#### config_generator.py
- Line 15: unused variable 'PROG_NAME' (60% confidence) (UNUSED)

#### main.py
- Line 19: unused variable 'BASE_CONFIG' (60% confidence) (UNUSED)
- Line 104: unused function '_running_under_virtualenv' (60% confidence) (UNUSED)

#### config.py
- Line 103: unused method 'get_setting' (60% confidence) (UNUSED)

#### constants.py
- Line 24: unused variable 'FALSE_VALUES' (60% confidence) (UNUSED)

#### context.py
- Line 124: unused property 'string_val_as_escaped_bytes' (60% confidence) (UNUSED)
- Line 284: unused method 'is_module_being_imported' (60% confidence) (UNUSED)

#### issue.py
- Line 59: unused method 'as_jsons' (60% confidence) (UNUSED)

#### tester.py
- Line 13: unused attribute 'formatwarning' (60% confidence) (UNUSED)
- Line 21: unused attribute 'last_result' (60% confidence) (UNUSED)

#### utils.py
- Line 323: unused function 'get_path_for_function' (60% confidence) (UNUSED)

#### sarif.py
- Line 302: unused attribute 'context_region' (60% confidence) (UNUSED)

#### app_debug.py
- Line 49: unused function 'flask_debug_true' (60% confidence) (UNUSED)

#### asserts.py
- Line 67: unused function 'assert_used' (60% confidence) (UNUSED)

#### crypto_request_no_cert_validation.py
- Line 54: unused function 'request_with_no_cert_validation' (60% confidence) (UNUSED)

#### django_sql_injection.py
- Line 20: unused function 'django_extra_used' (60% confidence) (UNUSED)
- Line 100: unused function 'django_rawsql_used' (60% confidence) (UNUSED)

#### django_xss.py
- Line 232: unused function 'django_mark_safe' (60% confidence) (UNUSED)

#### exec.py
- Line 51: unused function 'exec_used' (60% confidence) (UNUSED)

#### general_bad_file_permissions.py
- Line 72: unused function 'set_bad_file_permissions' (60% confidence) (UNUSED)

#### general_bind_all_interfaces.py
- Line 43: unused function 'hardcoded_bind_all_interfaces' (60% confidence) (UNUSED)

#### general_hardcoded_password.py
- Line 27: unused function 'hardcoded_password_string' (60% confidence) (UNUSED)
- Line 127: unused function 'hardcoded_password_funcarg' (60% confidence) (UNUSED)
- Line 183: unused function 'hardcoded_password_default' (60% confidence) (UNUSED)

#### general_hardcoded_tmp.py
- Line 65: unused function 'hardcoded_tmp_directory' (60% confidence) (UNUSED)

#### injection_paramiko.py
- Line 48: unused function 'paramiko_calls' (60% confidence) (UNUSED)

#### injection_shell.py
- Line 101: unused function 'subprocess_popen_with_shell_equals_true' (60% confidence) (UNUSED)
- Line 228: unused function 'subprocess_without_shell_equals_true' (60% confidence) (UNUSED)
- Line 314: unused function 'any_other_function_with_shell_equals_true' (60% confidence) (UNUSED)
- Line 399: unused function 'start_process_with_a_shell' (60% confidence) (UNUSED)
- Line 502: unused function 'start_process_with_no_shell' (60% confidence) (UNUSED)
- Line 596: unused function 'start_process_with_partial_path' (60% confidence) (UNUSED)

#### injection_sql.py
- Line 128: unused function 'hardcoded_sql_expressions' (60% confidence) (UNUSED)

#### injection_wildcard.py
- Line 110: unused function 'linux_commands_wildcard_injection' (60% confidence) (UNUSED)

#### insecure_ssl_tls.py
- Line 31: unused function 'ssl_with_bad_version' (60% confidence) (UNUSED)
- Line 157: unused function 'ssl_with_bad_defaults' (60% confidence) (UNUSED)
- Line 223: unused function 'ssl_with_no_version' (60% confidence) (UNUSED)

#### jinja2_templates.py
- Line 73: unused function 'jinja2_autoescape_false' (60% confidence) (UNUSED)

#### logging_config_insecure_listen.py
- Line 46: unused function 'logging_config_insecure_listen' (60% confidence) (UNUSED)

#### mako_templates.py
- Line 50: unused function 'use_of_mako_templates' (60% confidence) (UNUSED)

#### markupsafe_markup_xss.py
- Line 87: unused function 'markupsafe_markup_xss' (60% confidence) (UNUSED)

#### pytorch_load.py
- Line 48: unused function 'pytorch_load' (60% confidence) (UNUSED)

#### request_without_timeout.py
- Line 55: unused function 'request_without_timeout' (60% confidence) (UNUSED)

#### snmp_security_check.py
- Line 10: unused function 'snmp_insecure_version_check' (60% confidence) (UNUSED)
- Line 61: unused function 'snmp_crypto_check' (60% confidence) (UNUSED)

#### ssh_no_host_key_verification.py
- Line 45: unused function 'ssh_no_host_key_verification' (60% confidence) (UNUSED)

#### tarfile_unsafe_members.py
- Line 104: unused function 'tarfile_unsafe_members' (60% confidence) (UNUSED)

#### trojansource.py
- Line 54: unused function 'trojansource' (60% confidence) (UNUSED)

#### try_except_continue.py
- Line 89: unused function 'try_except_continue' (60% confidence) (UNUSED)

#### try_except_pass.py
- Line 87: unused function 'try_except_pass' (60% confidence) (UNUSED)

#### weak_cryptographic_key.py
- Line 159: unused function 'weak_cryptographic_key' (60% confidence) (UNUSED)

#### yaml_load.py
- Line 49: unused function 'yaml_load' (60% confidence) (UNUSED)

#### base.py
- Line 141: unused method 'connect_via' (60% confidence) (UNUSED)
- Line 167: unused method 'connected_to' (60% confidence) (UNUSED)
- Line 255: unused function 'send_async' (60% confidence) (UNUSED)
- Line 430: unused method '_cleanup_bookkeeping' (60% confidence) (UNUSED)
- Line 456: unused method '_clear_state' (60% confidence) (UNUSED)

#### __init__.py
- Line 668: unused attribute 'cache_lock' (60% confidence) (UNUSED)
- Line 733: unused attribute 'cache_lock' (60% confidence) (UNUSED)

#### constant.py
- Line 404: unused variable 'IANA_SUPPORTED_COUNT' (60% confidence) (UNUSED)

#### md.py
- Line 67: unused class 'TooManySymbolOrPunctuationPlugin' (60% confidence) (UNUSED)
- Line 74: unused attribute '_frenzy_symbol_in_word' (60% confidence) (UNUSED)
- Line 114: unused class 'TooManyAccentuatedPlugin' (60% confidence) (UNUSED)
- Line 141: unused class 'UnprintablePlugin' (60% confidence) (UNUSED)
- Line 165: unused class 'SuspiciousDuplicateAccentPlugin' (60% confidence) (UNUSED)
- Line 202: unused class 'SuspiciousRange' (60% confidence) (UNUSED)
- Line 251: unused class 'SuperWeirdWordPlugin' (60% confidence) (UNUSED)
- Line 254: unused attribute '_bad_word_count' (60% confidence) (UNUSED)
- Line 335: unused attribute '_bad_word_count' (60% confidence) (UNUSED)
- Line 355: unused attribute '_bad_word_count' (60% confidence) (UNUSED)
- Line 369: unused class 'CjkUncommonPlugin' (60% confidence) (UNUSED)
- Line 404: unused class 'ArchaicUpperLowerPlugin' (60% confidence) (UNUSED)
- Line 480: unused class 'ArabicIsolatedFormPlugin' (60% confidence) (UNUSED)

#### models.py
- Line 33: unused attribute '_mean_coherence_ratio' (60% confidence) (UNUSED)
- Line 116: unused property 'byte_order_mark' (60% confidence) (UNUSED)
- Line 181: unused property 'submatch' (60% confidence) (UNUSED)
- Line 185: unused property 'has_submatch' (60% confidence) (UNUSED)

#### utils.py
- Line 317: unused function 'cp_similarity' (60% confidence) (UNUSED)

#### _textwrap.py
- Line 9: unused method '_handle_long_word' (60% confidence) (UNUSED)

#### _winconsole.py
- Line 47: unused variable 'GetCommandLineW' (60% confidence) (UNUSED)
- Line 64: unused variable 'STDIN_FILENO' (60% confidence) (UNUSED)
- Line 65: unused variable 'STDOUT_FILENO' (60% confidence) (UNUSED)
- Line 66: unused variable 'STDERR_FILENO' (60% confidence) (UNUSED)

#### core.py
- Line 437: unused attribute '_close_callbacks' (60% confidence) (UNUSED)
- Line 442: unused property 'protected_args' (60% confidence) (UNUSED)
- Line 1590: unused variable '__func' (100% confidence) (UNUSED)
- Line 1639: unused variable '__func' (100% confidence) (UNUSED)
- Line 1944: unused method 'add_source' (60% confidence) (UNUSED)

#### decorators.py
- Line 100: unused function 'pass_meta_key' (60% confidence) (UNUSED)

#### shell_completion.py
- Line 414: unused function 'add_completion_class' (60% confidence) (UNUSED)
- Line 465: unused attribute 'whitespace_split' (60% confidence) (UNUSED)
- Line 466: unused attribute 'commenters' (60% confidence) (UNUSED)

#### testing.py
- Line 327: unused attribute '_CHUNK_SIZE' (60% confidence) (UNUSED)
- Line 528: unused method 'isolated_filesystem' (60% confidence) (UNUSED)

#### types.py
- Line 1162: unused variable 'envvars' (60% confidence) (UNUSED)

#### isoparser.py
- Line 148: unused method 'parse_isodate' (60% confidence) (UNUSED)
- Line 165: unused method 'parse_isotime' (60% confidence) (UNUSED)
- Line 181: unused method 'parse_tzstr' (60% confidence) (UNUSED)

#### rrule.py
- Line 230: unused method 'xafter' (60% confidence) (UNUSED)
- Line 1492: unused method '_handle_FREQ' (60% confidence) (UNUSED)
- Line 1495: unused method '_handle_UNTIL' (60% confidence) (UNUSED)
- Line 1506: unused method '_handle_WKST' (60% confidence) (UNUSED)

#### tz.py
- Line 38: unused variable 'EPOCHORDINAL' (60% confidence) (UNUSED)
- Line 262: unused variable 'fold_naive' (100% confidence) (UNUSED)
- Line 635: unused attribute 'ttinfo_before' (60% confidence) (UNUSED)
- Line 638: unused attribute 'ttinfo_first' (60% confidence) (UNUSED)
- Line 655: unused attribute 'ttinfo_before' (60% confidence) (UNUSED)
- Line 658: unused attribute 'ttinfo_before' (60% confidence) (UNUSED)
- Line 1579: unused method 'set_cache_size' (60% confidence) (UNUSED)

#### utils.py
- Line 29: unused function 'default_tzinfo' (60% confidence) (UNUSED)
- Line 64: unused function 'within_delta' (60% confidence) (UNUSED)

#### __init__.py
- Line 114: unused function 'citation' (60% confidence) (UNUSED)

#### _dill.py
- Line 42: unused import '_trace' (90% confidence) (UNUSED)
- Line 49: unused variable 'OLD38' (60% confidence) (UNUSED)
- Line 70: unused variable 'BufferType' (60% confidence) (UNUSED)
- Line 102: unused variable 'NumpyUfuncType' (60% confidence) (UNUSED)
- Line 108: unused variable 'NumpyUfuncType' (60% confidence) (UNUSED)
- Line 115: unused import 'NumpyUfuncType' (90% confidence) (UNUSED)
- Line 382: unused function 'save_numpy_ufunc' (60% confidence) (UNUSED)
- Line 396: unused function 'save_numpy_dtype' (60% confidence) (UNUSED)
- Line 409: unused function 'save_numpy_array' (60% confidence) (UNUSED)
- Line 594: unused function '_unmarshal' (60% confidence) (UNUSED)
- Line 789: unused function '_create_ftype' (60% confidence) (UNUSED)
- Line 913: unused class '_itemgetter_helper' (60% confidence) (UNUSED)
- Line 920: unused class '_attrgetter_helper' (60% confidence) (UNUSED)
- Line 1049: unused method '_get_attr' (60% confidence) (UNUSED)
- Line 1168: unused function 'save_code' (60% confidence) (UNUSED)
- Line 1240: unused function 'save_module_dict' (60% confidence) (UNUSED)
- Line 1322: unused function 'save_classobj' (60% confidence) (UNUSED)
- Line 1337: unused function 'save_generic_alias' (60% confidence) (UNUSED)
- Line 1355: unused function 'save_thread_handle' (60% confidence) (UNUSED)
- Line 1362: unused function 'save_lock' (60% confidence) (UNUSED)
- Line 1369: unused function 'save_rlock' (60% confidence) (UNUSED)
- Line 1380: unused function 'save_socket' (60% confidence) (UNUSED)
- Line 1413: unused function 'save_file' (60% confidence) (UNUSED)
- Line 1424: unused function 'save_file' (60% confidence) (UNUSED)
- Line 1432: unused function 'save_file' (60% confidence) (UNUSED)
- Line 1442: unused function 'save_file' (60% confidence) (UNUSED)
- Line 1455: unused function 'save_stringi' (60% confidence) (UNUSED)
- Line 1467: unused function 'save_stringo' (60% confidence) (UNUSED)
- Line 1481: unused function 'save_lru_cache' (60% confidence) (UNUSED)
- Line 1498: unused function 'save_super' (60% confidence) (UNUSED)
- Line 1506: unused function 'save_instancemethod0' (60% confidence) (UNUSED)
- Line 1523: unused function 'save_instancemethod0' (60% confidence) (UNUSED)
- Line 1531: unused function 'save_wrapper_descriptor' (60% confidence) (UNUSED)
- Line 1543: unused function 'save_wrapper_descriptor' (60% confidence) (UNUSED)
- Line 1552: unused function 'save_cell' (60% confidence) (UNUSED)
- Line 1598: unused function 'save_dictproxy' (60% confidence) (UNUSED)
- Line 1606: unused function 'save_dictproxy' (60% confidence) (UNUSED)
- Line 1613: unused function 'save_slice' (60% confidence) (UNUSED)
- Line 1620: unused function 'save_singleton' (60% confidence) (UNUSED)
- Line 1666: unused function 'save_weakref' (60% confidence) (UNUSED)
- Line 1675: unused function 'save_weakproxy' (60% confidence) (UNUSED)
- Line 1707: unused function 'save_module' (60% confidence) (UNUSED)
- Line 1709: unsatisfiable 'if' condition (100% confidence) (UNUSED)
- Line 1930: unused function 'save_property' (60% confidence) (UNUSED)
- Line 1938: unused function 'save_classmethod' (60% confidence) (UNUSED)
- Line 1957: unused function 'save_function' (60% confidence) (UNUSED)
- Line 2106: unused function 'save_capsule' (60% confidence) (UNUSED)
- Line 2128: unused function 'save_dataclasses_HAS_DEFAULT_FACTORY_CLASS' (60% confidence) (UNUSED)
- Line 2135: unused function 'save_dataclasses_MISSING_TYPE' (60% confidence) (UNUSED)
- Line 2142: unused function 'save_dataclasses_KW_ONLY_TYPE' (60% confidence) (UNUSED)
- Line 2149: unused function 'save_dataclasses_FIELD_BASE' (60% confidence) (UNUSED)

#### pointers.py
- Line 119: unused variable 'refobject' (60% confidence) (UNUSED)

#### session.py
- Line 601: unused attribute '__session__' (60% confidence) (UNUSED)

#### source.py
- Line 476: unused function '_isstring' (60% confidence) (UNUSED)
- Line 487: unused variable 'nspaces' (60% confidence) (UNUSED)
- Line 1014: unused function 'likely_import' (60% confidence) (UNUSED)
- Line 1016: unused function '_likely_import' (60% confidence) (UNUSED)
- Line 1019: unused variable 'getblocks_from_history' (60% confidence) (UNUSED)

#### test_classdef.py
- Line 255: unused class 'metaclass_with_new' (60% confidence) (UNUSED)

#### test_functions.py
- Line 47: unsatisfiable 'if' condition (100% confidence) (UNUSED)
- Line 87: unused variable 'dumped_func_cache' (60% confidence) (UNUSED)

#### test_mixins.py
- Line 13: unused function 'wtf' (60% confidence) (UNUSED)

#### test_moduledict.py
- Line 33: unused variable 'unpicklable' (60% confidence) (UNUSED)

#### test_recursive.py
- Line 20: unreachable 'else' block (100% confidence) (UNUSED)

#### test_session.py
- Line 83: unused variable 'cubed' (60% confidence) (UNUSED)
- Line 120: unused function '_test_objects' (60% confidence) (UNUSED)
- Line 236: unused attribute 'AsyncCM' (60% confidence) (UNUSED)
- Line 237: unused attribute 'thread_exec' (60% confidence) (UNUSED)

#### distro.py
- Line 1119: unused attribute 'whitespace_split' (60% confidence) (UNUSED)

#### legacy.py
- Line 86: unused attribute '_file_checker_manager' (60% confidence) (UNUSED)

#### default.py
- Line 75: unused class 'Pylint' (60% confidence) (UNUSED)
- Line 81: unused class 'FilenameOnly' (60% confidence) (UNUSED)
- Line 102: unused class 'Nothing' (60% confidence) (UNUSED)

#### manager.py
- Line 292: unused method 'extend_default_ignore' (60% confidence) (UNUSED)

#### pycodestyle.py
- Line 40: unused function 'pycodestyle_logical' (60% confidence) (UNUSED)
- Line 87: unused function 'pycodestyle_physical' (60% confidence) (UNUSED)

#### pyflakes.py
- Line 66: unused class 'FlakesChecker' (60% confidence) (UNUSED)

#### __init__.py
- Line 260: unused variable 'GIT_OK' (60% confidence) (UNUSED)
- Line 285: unused variable 'GIT_OK' (60% confidence) (UNUSED)
- Line 292: unused variable 'GIT_OK' (60% confidence) (UNUSED)

#### cmd.py
- Line 433: unused variable 'USE_SHELL' (60% confidence) (UNUSED)
- Line 988: unused method 'set_persistent_git_options' (60% confidence) (UNUSED)
- Line 1431: unused method 'custom_environment' (60% confidence) (UNUSED)
- Line 1681: unused method 'get_object_data' (60% confidence) (UNUSED)

#### compat.py
- Line 69: unused variable 'is_win' (60% confidence) (UNUSED)
- Line 81: unused variable 'is_posix' (60% confidence) (UNUSED)
- Line 94: unused variable 'is_darwin' (60% confidence) (UNUSED)
- Line 129: unused function 'safe_encode' (60% confidence) (UNUSED)
- Line 133: unused function 'safe_encode' (60% confidence) (UNUSED)
- Line 137: unused function 'safe_encode' (60% confidence) (UNUSED)
- Line 149: unused function 'win_encode' (60% confidence) (UNUSED)
- Line 153: unused function 'win_encode' (60% confidence) (UNUSED)
- Line 157: unused function 'win_encode' (60% confidence) (UNUSED)

#### config.py
- Line 891: unused method 'add_value' (60% confidence) (UNUSED)

#### diff.py
- Line 302: unused method 'iter_change_type' (60% confidence) (UNUSED)

#### base.py
- Line 254: unused method 'merge_tree' (60% confidence) (UNUSED)
- Line 522: unused method 'unmerged_blobs' (60% confidence) (UNUSED)
- Line 547: unused method 'resolve_blobs' (60% confidence) (UNUSED)

#### typ.py
- Line 31: unused variable 'CE_EXTENDED' (60% confidence) (UNUSED)
- Line 32: unused variable 'CE_VALID' (60% confidence) (UNUSED)

#### blob.py
- Line 30: unused variable 'executable_mode' (60% confidence) (UNUSED)
- Line 31: unused variable 'file_mode' (60% confidence) (UNUSED)
- Line 32: unused variable 'link_mode' (60% confidence) (UNUSED)

#### commit.py
- Line 250: unused property 'authored_datetime' (60% confidence) (UNUSED)
- Line 254: unused property 'committed_datetime' (60% confidence) (UNUSED)
- Line 351: unused method 'iter_parents' (60% confidence) (UNUSED)
- Line 401: unused property 'trailers' (60% confidence) (UNUSED)

#### base.py
- Line 1260: unused method 'set_parent_commit' (60% confidence) (UNUSED)

#### tree.py
- Line 80: unused method 'set_done' (60% confidence) (UNUSED)
- Line 139: unused method 'add_unchecked' (60% confidence) (UNUSED)
- Line 282: unused property 'blobs' (60% confidence) (UNUSED)
- Line 340: unused method 'list_traverse' (60% confidence) (UNUSED)

#### util.py
- Line 361: unused attribute '_proc' (60% confidence) (UNUSED)
- Line 400: unused method 'list_traverse' (60% confidence) (UNUSED)
- Line 619: unused method 'list_traverse' (60% confidence) (UNUSED)

#### head.py
- Line 55: unused method 'orig_head' (60% confidence) (UNUSED)

#### remote.py
- Line 282: unused method 'raise_if_error' (60% confidence) (UNUSED)
- Line 667: unused method 'add_url' (60% confidence) (UNUSED)
- Line 746: unused property 'stale_refs' (60% confidence) (UNUSED)

#### base.py
- Line 102: unused variable 'orig_linenos' (60% confidence) (UNUSED)
- Line 142: unused variable 're_tab_full_line' (60% confidence) (UNUSED)
- Line 502: unused method 'create_submodule' (60% confidence) (UNUSED)
- Line 514: unused method 'iter_submodules' (60% confidence) (UNUSED)
- Line 525: unused method 'submodule_update' (60% confidence) (UNUSED)
- Line 569: unused method 'create_head' (60% confidence) (UNUSED)
- Line 587: unused method 'delete_head' (60% confidence) (UNUSED)
- Line 595: unused method 'create_tag' (60% confidence) (UNUSED)
- Line 614: unused method 'delete_tag' (60% confidence) (UNUSED)
- Line 728: unused method 'iter_trees' (60% confidence) (UNUSED)
- Line 834: unused method 'is_ancestor' (60% confidence) (UNUSED)
- Line 854: unused method 'is_valid_object' (60% confidence) (UNUSED)
- Line 888: unused variable 'daemon_export' (60% confidence) (UNUSED)
- Line 932: unused variable 'alternates' (60% confidence) (UNUSED)
- Line 1185: unused variable 'committer_email' (60% confidence) (UNUSED)
- Line 1186: unused variable 'committer_date' (60% confidence) (UNUSED)
- Line 1623: unused method 'currently_rebasing_on' (60% confidence) (UNUSED)

#### types.py
- Line 133: unused variable 'Lit_commit_ish' (60% confidence) (UNUSED)
- Line 274: unused class 'Has_Repo' (60% confidence) (UNUSED)

#### util.py
- Line 158: unused variable 'HIDE_WINDOWS_FREEZE_ERRORS' (60% confidence) (UNUSED)
- Line 440: unused function 'decygpath' (60% confidence) (UNUSED)
- Line 581: unused variable 'OP_MASK' (60% confidence) (UNUSED)

#### loose.py
- Line 142: unreachable code after 'try' (100% confidence) (UNUSED)

#### fun.py
- Line 63: unused function '_set_delta_rbound' (60% confidence) (UNUSED)
- Line 93: unused function 'delta_duplicate' (60% confidence) (UNUSED)
- Line 291: unused method 'check_integrity' (60% confidence) (UNUSED)

#### pack.py
- Line 269: unused attribute '_packfile_checksum' (60% confidence) (UNUSED)
- Line 271: unused attribute '_packfile_checksum' (60% confidence) (UNUSED)
- Line 307: unused method '_entry_v1' (60% confidence) (UNUSED)
- Line 311: unused method '_offset_v1' (60% confidence) (UNUSED)
- Line 315: unused method '_sha_v1' (60% confidence) (UNUSED)
- Line 320: unused method '_crc_v1' (60% confidence) (UNUSED)
- Line 327: unused method '_entry_v2' (60% confidence) (UNUSED)
- Line 851: unreachable code after 'if' (100% confidence) (UNUSED)
- Line 1019: unused variable 'index_binsha' (60% confidence) (UNUSED)

#### stream.py
- Line 67: unused variable 'max_read_size' (60% confidence) (UNUSED)
- Line 357: unused variable 'k_max_memory_move' (60% confidence) (UNUSED)

#### lib.py
- Line 91: unused function 'with_packs_rw' (60% confidence) (UNUSED)
- Line 153: unused function 'make_memory_file' (60% confidence) (UNUSED)

#### test_pack.py
- Line 36: unused function 'bin_sha_from_filename' (60% confidence) (UNUSED)

#### util.py
- Line 212: unused function 'sliding_ro_buffer' (60% confidence) (UNUSED)

#### any.py
- Line 37: unused function 'unpack_as' (60% confidence) (UNUSED)

#### api_pb2.py
- Line 25: unused import 'google_dot_protobuf_dot_source__context__pb2' (90% confidence) (UNUSED)
- Line 26: unused import 'google_dot_protobuf_dot_type__pb2' (90% confidence) (UNUSED)

#### plugin_pb2.py
- Line 25: unused import 'google_dot_protobuf_dot_descriptor__pb2' (90% confidence) (UNUSED)

#### descriptor.py
- Line 58: unused class '_Lock' (60% confidence) (UNUSED)
- Line 436: unused property 'fields_by_camelcase_name' (60% confidence) (UNUSED)
- Line 446: unused method 'EnumValueName' (60% confidence) (UNUSED)
- Line 558: unused variable 'MAX_TYPE' (60% confidence) (UNUSED)
- Line 604: unused variable 'MAX_LABEL' (60% confidence) (UNUSED)
- Line 608: unused variable 'MAX_FIELD_NUMBER' (60% confidence) (UNUSED)
- Line 667: unused attribute '_cdescriptor' (60% confidence) (UNUSED)
- Line 670: unused attribute '_cdescriptor' (60% confidence) (UNUSED)
- Line 672: unused attribute '_cdescriptor' (60% confidence) (UNUSED)

#### descriptor_database.py
- Line 138: unused variable 'extendee_name' (100% confidence) (UNUSED)
- Line 138: unused variable 'extension_number' (100% confidence) (UNUSED)
- Line 142: unused variable 'extendee_name' (100% confidence) (UNUSED)

#### descriptor_pool.py
- Line 93: unused variable 'use_deprecated_legacy_json_field_conflicts' (100% confidence) (UNUSED)
- Line 668: unused method 'SetFeatureSetDefaults' (60% confidence) (UNUSED)

#### duration.py
- Line 15: unused function 'from_json_string' (60% confidence) (UNUSED)
- Line 31: unused function 'from_microseconds' (60% confidence) (UNUSED)
- Line 38: unused function 'from_milliseconds' (60% confidence) (UNUSED)
- Line 45: unused function 'from_nanoseconds' (60% confidence) (UNUSED)
- Line 52: unused function 'from_seconds' (60% confidence) (UNUSED)
- Line 59: unused function 'from_timedelta' (60% confidence) (UNUSED)
- Line 66: unused function 'to_json_string' (60% confidence) (UNUSED)
- Line 83: unused function 'to_milliseconds' (60% confidence) (UNUSED)
- Line 88: unused function 'to_nanoseconds' (60% confidence) (UNUSED)

#### api_implementation.py
- Line 120: unused import 'enable_deterministic_proto_serialization' (90% confidence) (UNUSED)

#### builder.py
- Line 90: unused function 'AddHelpersToExtensions' (60% confidence) (UNUSED)
- Line 100: unused function 'BuildServices' (60% confidence) (UNUSED)

#### containers.py
- Line 202: unused variable 'unused_memo' (100% confidence) (UNUSED)
- Line 484: unused method 'get_or_create' (60% confidence) (UNUSED)

#### encoder.py
- Line 352: unused variable 'unused_deterministic' (100% confidence) (UNUSED)
- Line 370: unused variable 'unused_deterministic' (100% confidence) (UNUSED)
- Line 505: unused variable 'unused_deterministic' (100% confidence) (UNUSED)
- Line 512: unused variable 'unused_deterministic' (100% confidence) (UNUSED)
- Line 576: unused variable 'unused_deterministic' (100% confidence) (UNUSED)
- Line 586: unused variable 'unused_deterministic' (100% confidence) (UNUSED)
- Line 643: unused variable 'unused_deterministic' (100% confidence) (UNUSED)
- Line 653: unused variable 'unused_deterministic' (100% confidence) (UNUSED)

#### field_mask.py
- Line 34: unused method 'IsValidForDescriptor' (60% confidence) (UNUSED)
- Line 41: unused method 'AllFieldsFromDescriptor' (60% confidence) (UNUSED)
- Line 47: unused method 'CanonicalFormFromMask' (60% confidence) (UNUSED)
- Line 68: unused method 'Intersect' (60% confidence) (UNUSED)

#### message_listener.py
- Line 17: unused class 'MessageListener' (60% confidence) (UNUSED)

#### python_message.py
- Line 1060: unused variable 'unused_message_descriptor' (100% confidence) (UNUSED)
- Line 1083: unused function '_BytesForNonRepeatedElement' (60% confidence) (UNUSED)
- Line 1431: unused method '_UnknownFields' (60% confidence) (UNUSED)

#### testing_refleaks.py
- Line 40: unused method 'addDuration' (60% confidence) (UNUSED)
- Line 116: unused variable 'SkipReferenceLeakChecker' (60% confidence) (UNUSED)
- Line 124: unused function 'SkipReferenceLeakChecker' (60% confidence) (UNUSED)

#### well_known_types.py
- Line 182: unused method 'GetCurrentTime' (60% confidence) (UNUSED)
- Line 601: unused method 'get_or_create_list' (60% confidence) (UNUSED)
- Line 608: unused method 'get_or_create_struct' (60% confidence) (UNUSED)
- Line 668: unused method 'add_struct' (60% confidence) (UNUSED)
- Line 675: unused method 'add_list' (60% confidence) (UNUSED)

#### wire_format.py
- Line 34: unused variable 'INT32_MAX' (60% confidence) (UNUSED)
- Line 35: unused variable 'INT32_MIN' (60% confidence) (UNUSED)
- Line 36: unused variable 'UINT32_MAX' (60% confidence) (UNUSED)
- Line 45: unused variable 'FORMAT_FLOAT_LITTLE_ENDIAN' (60% confidence) (UNUSED)
- Line 46: unused variable 'FORMAT_DOUBLE_LITTLE_ENDIAN' (60% confidence) (UNUSED)
- Line 103: unused function 'Int32ByteSizeNoTag' (60% confidence) (UNUSED)
- Line 128: unused variable 'fixed32' (100% confidence) (UNUSED)
- Line 132: unused variable 'fixed64' (100% confidence) (UNUSED)
- Line 136: unused variable 'sfixed32' (100% confidence) (UNUSED)
- Line 140: unused variable 'sfixed64' (100% confidence) (UNUSED)
- Line 181: unused function 'MessageSetItemByteSize' (60% confidence) (UNUSED)

#### json_format.py
- Line 79: unused function 'MessageToJson' (60% confidence) (UNUSED)
- Line 326: unused method '_AnyMessageToJsonObject' (60% confidence) (UNUSED)
- Line 348: unused method '_GenericMessageToJsonObject' (60% confidence) (UNUSED)
- Line 384: unused method '_StructMessageToJsonObject' (60% confidence) (UNUSED)
- Line 706: unused method '_ConvertAnyMessage' (60% confidence) (UNUSED)
- Line 744: unused method '_ConvertGenericMessage' (60% confidence) (UNUSED)

#### message.py
- Line 104: unused variable 'field_name_or_key' (100% confidence) (UNUSED)
- Line 326: unused variable 'oneof_group' (100% confidence) (UNUSED)
- Line 368: unused method 'UnknownFields' (60% confidence) (UNUSED)

#### message_factory.py
- Line 138: unused variable 'extended_class' (60% confidence) (UNUSED)
- Line 154: unused class 'MessageFactory' (60% confidence) (UNUSED)
- Line 162: unused function 'GetMessages' (60% confidence) (UNUSED)

#### proto.py
- Line 49: unused function 'serialize_length_prefixed' (60% confidence) (UNUSED)
- Line 79: unused function 'parse_length_prefixed' (60% confidence) (UNUSED)
- Line 119: unused function 'byte_size' (60% confidence) (UNUSED)
- Line 131: unused function 'clear_message' (60% confidence) (UNUSED)
- Line 140: unused function 'clear_field' (60% confidence) (UNUSED)

#### proto_builder.py
- Line 36: unused function 'MakeSimpleProtoClass' (60% confidence) (UNUSED)

#### reflection.py
- Line 36: unused variable 'MESSAGE_CLASS_CACHE' (60% confidence) (UNUSED)

#### runtime_version.py
- Line 22: unused variable 'GOOGLE_INTERNAL' (60% confidence) (UNUSED)

#### service_reflection.py
- Line 139: unused attribute 'GetRequestClass' (60% confidence) (UNUSED)
- Line 140: unused attribute 'GetResponseClass' (60% confidence) (UNUSED)

#### symbol_database.py
- Line 96: unused method 'RegisterServiceDescriptor' (60% confidence) (UNUSED)
- Line 135: unused method 'GetMessages' (60% confidence) (UNUSED)

#### text_format.py
- Line 73: unused method 'GetLine' (60% confidence) (UNUSED)
- Line 76: unused method 'GetColumn' (60% confidence) (UNUSED)
- Line 1320: unused attribute '_token_start' (60% confidence) (UNUSED)
- Line 1402: unused method 'ConsumeCommentOrTrailingComment' (60% confidence) (UNUSED)
- Line 1440: unused method 'TryConsumeIdentifierOrNumber' (60% confidence) (UNUSED)
- Line 1462: unused method 'TryConsumeInteger' (60% confidence) (UNUSED)

#### timestamp.py
- Line 16: unused function 'from_json_string' (60% confidence) (UNUSED)
- Line 32: unused function 'from_microseconds' (60% confidence) (UNUSED)
- Line 39: unused function 'from_milliseconds' (60% confidence) (UNUSED)
- Line 46: unused function 'from_nanoseconds' (60% confidence) (UNUSED)
- Line 53: unused function 'from_seconds' (60% confidence) (UNUSED)
- Line 60: unused function 'from_current_time' (60% confidence) (UNUSED)
- Line 67: unused function 'to_json_string' (60% confidence) (UNUSED)
- Line 83: unused function 'to_milliseconds' (60% confidence) (UNUSED)
- Line 88: unused function 'to_nanoseconds' (60% confidence) (UNUSED)

#### type_pb2.py
- Line 25: unused import 'google_dot_protobuf_dot_any__pb2' (90% confidence) (UNUSED)
- Line 26: unused import 'google_dot_protobuf_dot_source__context__pb2' (90% confidence) (UNUSED)

#### __init__.py
- Line 35: unused variable 'PRODUCT_ID' (60% confidence) (UNUSED)

#### _abnf.py
- Line 8: unused variable 'OWS' (60% confidence) (UNUSED)
- Line 54: unused variable 'vchar' (60% confidence) (UNUSED)
- Line 57: unused variable 'field_content' (60% confidence) (UNUSED)
- Line 112: unused variable 'HEXDIG' (60% confidence) (UNUSED)
- Line 124: unused variable 'chunk_ext' (60% confidence) (UNUSED)

#### _connection.py
- Line 231: unused property 'they_are_waiting_for_100_continue' (60% confidence) (UNUSED)
- Line 577: unused method 'send_failed' (60% confidence) (UNUSED)

#### http11.py
- Line 29: unused variable 'H11SendEvent' (60% confidence) (UNUSED)

#### http11.py
- Line 29: unused variable 'H11SendEvent' (60% confidence) (UNUSED)

#### _content.py
- Line 104: unreachable code after 'raise' (100% confidence) (UNUSED)

#### _status_codes.py
- Line 89: unused variable 'SWITCHING_PROTOCOLS' (60% confidence) (UNUSED)
- Line 90: unused variable 'PROCESSING' (60% confidence) (UNUSED)
- Line 91: unused variable 'EARLY_HINTS' (60% confidence) (UNUSED)
- Line 96: unused variable 'ACCEPTED' (60% confidence) (UNUSED)
- Line 97: unused variable 'NON_AUTHORITATIVE_INFORMATION' (60% confidence) (UNUSED)
- Line 98: unused variable 'NO_CONTENT' (60% confidence) (UNUSED)
- Line 99: unused variable 'RESET_CONTENT' (60% confidence) (UNUSED)
- Line 100: unused variable 'PARTIAL_CONTENT' (60% confidence) (UNUSED)
- Line 101: unused variable 'MULTI_STATUS' (60% confidence) (UNUSED)
- Line 102: unused variable 'ALREADY_REPORTED' (60% confidence) (UNUSED)
- Line 103: unused variable 'IM_USED' (60% confidence) (UNUSED)
- Line 106: unused variable 'MULTIPLE_CHOICES' (60% confidence) (UNUSED)
- Line 110: unused variable 'NOT_MODIFIED' (60% confidence) (UNUSED)
- Line 111: unused variable 'USE_PROXY' (60% confidence) (UNUSED)
- Line 116: unused variable 'BAD_REQUEST' (60% confidence) (UNUSED)
- Line 117: unused variable 'UNAUTHORIZED' (60% confidence) (UNUSED)
- Line 118: unused variable 'PAYMENT_REQUIRED' (60% confidence) (UNUSED)
- Line 119: unused variable 'FORBIDDEN' (60% confidence) (UNUSED)
- Line 121: unused variable 'METHOD_NOT_ALLOWED' (60% confidence) (UNUSED)
- Line 122: unused variable 'NOT_ACCEPTABLE' (60% confidence) (UNUSED)
- Line 123: unused variable 'PROXY_AUTHENTICATION_REQUIRED' (60% confidence) (UNUSED)
- Line 124: unused variable 'REQUEST_TIMEOUT' (60% confidence) (UNUSED)
- Line 125: unused variable 'CONFLICT' (60% confidence) (UNUSED)
- Line 126: unused variable 'GONE' (60% confidence) (UNUSED)
- Line 127: unused variable 'LENGTH_REQUIRED' (60% confidence) (UNUSED)
- Line 128: unused variable 'PRECONDITION_FAILED' (60% confidence) (UNUSED)
- Line 129: unused variable 'REQUEST_ENTITY_TOO_LARGE' (60% confidence) (UNUSED)
- Line 130: unused variable 'REQUEST_URI_TOO_LONG' (60% confidence) (UNUSED)
- Line 131: unused variable 'UNSUPPORTED_MEDIA_TYPE' (60% confidence) (UNUSED)
- Line 132: unused variable 'REQUESTED_RANGE_NOT_SATISFIABLE' (60% confidence) (UNUSED)
- Line 133: unused variable 'EXPECTATION_FAILED' (60% confidence) (UNUSED)
- Line 134: unused variable 'IM_A_TEAPOT' (60% confidence) (UNUSED)
- Line 135: unused variable 'MISDIRECTED_REQUEST' (60% confidence) (UNUSED)
- Line 136: unused variable 'UNPROCESSABLE_ENTITY' (60% confidence) (UNUSED)
- Line 137: unused variable 'LOCKED' (60% confidence) (UNUSED)
- Line 138: unused variable 'FAILED_DEPENDENCY' (60% confidence) (UNUSED)
- Line 139: unused variable 'TOO_EARLY' (60% confidence) (UNUSED)
- Line 140: unused variable 'UPGRADE_REQUIRED' (60% confidence) (UNUSED)
- Line 141: unused variable 'PRECONDITION_REQUIRED' (60% confidence) (UNUSED)
- Line 142: unused variable 'TOO_MANY_REQUESTS' (60% confidence) (UNUSED)
- Line 143: unused variable 'REQUEST_HEADER_FIELDS_TOO_LARGE' (60% confidence) (UNUSED)
- Line 144: unused variable 'UNAVAILABLE_FOR_LEGAL_REASONS' (60% confidence) (UNUSED)
- Line 147: unused variable 'INTERNAL_SERVER_ERROR' (60% confidence) (UNUSED)
- Line 148: unused variable 'NOT_IMPLEMENTED' (60% confidence) (UNUSED)
- Line 149: unused variable 'BAD_GATEWAY' (60% confidence) (UNUSED)
- Line 150: unused variable 'SERVICE_UNAVAILABLE' (60% confidence) (UNUSED)
- Line 151: unused variable 'GATEWAY_TIMEOUT' (60% confidence) (UNUSED)
- Line 152: unused variable 'HTTP_VERSION_NOT_SUPPORTED' (60% confidence) (UNUSED)
- Line 153: unused variable 'VARIANT_ALSO_NEGOTIATES' (60% confidence) (UNUSED)
- Line 154: unused variable 'INSUFFICIENT_STORAGE' (60% confidence) (UNUSED)
- Line 155: unused variable 'LOOP_DETECTED' (60% confidence) (UNUSED)
- Line 156: unused variable 'NOT_EXTENDED' (60% confidence) (UNUSED)
- Line 157: unused variable 'NETWORK_AUTHENTICATION_REQUIRED' (60% confidence) (UNUSED)

#### _types.py
- Line 33: unused variable 'URLTypes' (60% confidence) (UNUSED)
- Line 97: unreachable code after 'raise' (100% confidence) (UNUSED)
- Line 111: unreachable code after 'raise' (100% confidence) (UNUSED)

#### _urls.py
- Line 342: unused method 'copy_set_param' (60% confidence) (UNUSED)
- Line 345: unused method 'copy_add_param' (60% confidence) (UNUSED)
- Line 348: unused method 'copy_remove_param' (60% confidence) (UNUSED)
- Line 351: unused method 'copy_merge_params' (60% confidence) (UNUSED)

#### codec.py
- Line 31: unused method '_buffer_encode' (60% confidence) (UNUSED)
- Line 65: unused method '_buffer_decode' (60% confidence) (UNUSED)

#### compat.py
- Line 6: unused function 'ToASCII' (60% confidence) (UNUSED)
- Line 10: unused function 'ToUnicode' (60% confidence) (UNUSED)
- Line 14: unused function 'nameprep' (60% confidence) (UNUSED)

#### intranges.py
- Line 12: unused function 'intranges_from_list' (60% confidence) (UNUSED)

#### hooks.py
- Line 35: unused function 'git_hook' (60% confidence) (UNUSED)

#### literal.py
- Line 97: unused function '_unique_list' (60% confidence) (UNUSED)
- Line 112: unused function '_unique_tuple' (60% confidence) (UNUSED)

#### main.py
- Line 974: unused function 'identify_imports_main' (60% confidence) (UNUSED)

#### settings.py
- Line 160: unused variable 'known_future_library' (60% confidence) (UNUSED)
- Line 162: unused variable 'known_first_party' (60% confidence) (UNUSED)
- Line 163: unused variable 'known_local_folder' (60% confidence) (UNUSED)
- Line 165: unused variable 'extra_standard_library' (60% confidence) (UNUSED)
- Line 244: unused variable 'import_dependencies' (60% confidence) (UNUSED)

#### setuptools_commands.py
- Line 13: unused class 'ISortCommand' (60% confidence) (UNUSED)

#### wrap_modes.py
- Line 23: unused variable 'white_space' (100% confidence) (UNUSED)
- Line 30: unused variable 'remove_comments' (100% confidence) (UNUSED)
- Line 41: unused attribute '__signature__' (60% confidence) (UNUSED)
- Line 221: unused function 'vertical_grid' (60% confidence) (UNUSED)
- Line 235: unused function 'vertical_grid_grouped_no_comma' (60% confidence) (UNUSED)
- Line 262: unused function 'vertical_hanging_indent_bracket' (60% confidence) (UNUSED)
- Line 270: unused function 'vertical_prefix_from_module_import' (60% confidence) (UNUSED)
- Line 310: unused function 'hanging_indent_with_parentheses' (60% confidence) (UNUSED)
- Line 366: unused function 'backslash_grid' (60% confidence) (UNUSED)

#### bccache.py
- Line 27: unused class '_MemcachedClient' (60% confidence) (UNUSED)

#### compiler.py
- Line 263: unused method 'visit_Test' (60% confidence) (UNUSED)
- Line 267: unused method 'visit_Block' (60% confidence) (UNUSED)
- Line 289: unused method 'visit_Block' (60% confidence) (UNUSED)
- Line 316: unused attribute 'created_block_context' (60% confidence) (UNUSED)
- Line 829: unused method 'visit_Template' (60% confidence) (UNUSED)
- Line 951: unused method 'visit_Block' (60% confidence) (UNUSED)
- Line 1000: unused method 'visit_Extends' (60% confidence) (UNUSED)
- Line 1042: unused method 'visit_Include' (60% confidence) (UNUSED)
- Line 1126: unused method 'visit_FromImport' (60% confidence) (UNUSED)
- Line 1341: unused method 'visit_Macro' (60% confidence) (UNUSED)
- Line 1351: unused method 'visit_CallBlock' (60% confidence) (UNUSED)
- Line 1359: unused method 'visit_FilterBlock' (60% confidence) (UNUSED)
- Line 1382: unused method 'visit_ExprStmt' (60% confidence) (UNUSED)
- Line 1503: unused method 'visit_Output' (60% confidence) (UNUSED)
- Line 1613: unused method 'visit_AssignBlock' (60% confidence) (UNUSED)
- Line 1662: unused method 'visit_NSRef' (60% confidence) (UNUSED)
- Line 1670: unused method 'visit_Const' (60% confidence) (UNUSED)
- Line 1677: unused method 'visit_TemplateData' (60% confidence) (UNUSED)
- Line 1712: unused variable 'visit_Add' (60% confidence) (UNUSED)
- Line 1713: unused variable 'visit_Sub' (60% confidence) (UNUSED)
- Line 1714: unused variable 'visit_Mul' (60% confidence) (UNUSED)
- Line 1715: unused variable 'visit_Div' (60% confidence) (UNUSED)
- Line 1716: unused variable 'visit_FloorDiv' (60% confidence) (UNUSED)
- Line 1717: unused variable 'visit_Pow' (60% confidence) (UNUSED)
- Line 1718: unused variable 'visit_Mod' (60% confidence) (UNUSED)
- Line 1719: unused variable 'visit_And' (60% confidence) (UNUSED)
- Line 1720: unused variable 'visit_Or' (60% confidence) (UNUSED)
- Line 1721: unused variable 'visit_Pos' (60% confidence) (UNUSED)
- Line 1722: unused variable 'visit_Neg' (60% confidence) (UNUSED)
- Line 1723: unused variable 'visit_Not' (60% confidence) (UNUSED)
- Line 1725: unused method 'visit_Concat' (60% confidence) (UNUSED)
- Line 1747: unused method 'visit_Operand' (60% confidence) (UNUSED)
- Line 1751: unused method 'visit_Getattr' (60% confidence) (UNUSED)
- Line 1763: unused method 'visit_Getitem' (60% confidence) (UNUSED)
- Line 1853: unused method 'visit_Test' (60% confidence) (UNUSED)
- Line 1858: unused method 'visit_CondExpr' (60% confidence) (UNUSED)
- Line 1904: unused method 'visit_Keyword' (60% confidence) (UNUSED)
- Line 1910: unused method 'visit_MarkSafe' (60% confidence) (UNUSED)
- Line 1915: unused method 'visit_MarkSafeIfAutoescape' (60% confidence) (UNUSED)
- Line 1922: unused method 'visit_EnvironmentAttribute' (60% confidence) (UNUSED)
- Line 1927: unused method 'visit_ExtensionAttribute' (60% confidence) (UNUSED)
- Line 1932: unused method 'visit_ImportedName' (60% confidence) (UNUSED)
- Line 1935: unused method 'visit_InternalName' (60% confidence) (UNUSED)
- Line 1938: unused method 'visit_ContextReference' (60% confidence) (UNUSED)
- Line 1943: unused method 'visit_DerivedContextReference' (60% confidence) (UNUSED)
- Line 1948: unused method 'visit_Continue' (60% confidence) (UNUSED)
- Line 1951: unused method 'visit_Break' (60% confidence) (UNUSED)
- Line 1954: unused method 'visit_Scope' (60% confidence) (UNUSED)
- Line 1961: unused method 'visit_OverlayScope' (60% confidence) (UNUSED)
- Line 1988: unused method 'visit_ScopedEvalContextModifier' (60% confidence) (UNUSED)

#### environment.py
- Line 273: unused variable 'overlayed' (60% confidence) (UNUSED)
- Line 276: unused variable 'linked_to' (60% confidence) (UNUSED)
- Line 370: unused method 'add_extension' (60% confidence) (UNUSED)
- Line 434: unused attribute 'overlayed' (60% confidence) (UNUSED)
- Line 435: unused attribute 'linked_to' (60% confidence) (UNUSED)
- Line 773: unused method 'compile_expression' (60% confidence) (UNUSED)
- Line 818: unused method 'compile_templates' (60% confidence) (UNUSED)
- Line 1072: unused method 'get_or_select_template' (60% confidence) (UNUSED)
- Line 1452: unused method '_get_default_module_async' (60% confidence) (UNUSED)
- Line 1655: unused method 'enable_buffering' (60% confidence) (UNUSED)

#### ext.py
- Line 774: unused function 'babel_extract' (60% confidence) (UNUSED)
- Line 867: unused variable 'i18n' (60% confidence) (UNUSED)
- Line 869: unused variable 'loopcontrols' (60% confidence) (UNUSED)

#### filters.py
- Line 39: unused class 'HasHTML' (60% confidence) (UNUSED)
- Line 1380: unused function 'do_mark_unsafe' (60% confidence) (UNUSED)

#### idtracking.py
- Line 15: unused function 'find_symbols' (60% confidence) (UNUSED)
- Line 25: unused function 'symbols_for_node' (60% confidence) (UNUSED)
- Line 182: unused variable 'visit_Template' (60% confidence) (UNUSED)
- Line 183: unused variable 'visit_Block' (60% confidence) (UNUSED)
- Line 184: unused variable 'visit_Macro' (60% confidence) (UNUSED)
- Line 185: unused variable 'visit_FilterBlock' (60% confidence) (UNUSED)
- Line 186: unused variable 'visit_Scope' (60% confidence) (UNUSED)
- Line 188: unused variable 'visit_ScopedEvalContextModifier' (60% confidence) (UNUSED)
- Line 190: unused method 'visit_AssignBlock' (60% confidence) (UNUSED)
- Line 194: unused method 'visit_CallBlock' (60% confidence) (UNUSED)
- Line 198: unused method 'visit_OverlayScope' (60% confidence) (UNUSED)
- Line 249: unused method 'visit_NSRef' (60% confidence) (UNUSED)
- Line 270: unused method 'visit_Macro' (60% confidence) (UNUSED)
- Line 277: unused method 'visit_FromImport' (60% confidence) (UNUSED)
- Line 297: unused method 'visit_CallBlock' (60% confidence) (UNUSED)
- Line 300: unused method 'visit_FilterBlock' (60% confidence) (UNUSED)
- Line 307: unused method 'visit_AssignBlock' (60% confidence) (UNUSED)
- Line 311: unused method 'visit_Scope' (60% confidence) (UNUSED)
- Line 314: unused method 'visit_Block' (60% confidence) (UNUSED)
- Line 317: unused method 'visit_OverlayScope' (60% confidence) (UNUSED)

#### lexer.py
- Line 206: unused function 'count_newlines' (60% confidence) (UNUSED)

#### meta.py
- Line 34: unused function 'find_undeclared_variables' (60% confidence) (UNUSED)
- Line 62: unused function 'find_referenced_templates' (60% confidence) (UNUSED)

#### parser.py
- Line 160: unused method 'free_identifier' (60% confidence) (UNUSED)
- Line 225: unused method 'parse_set' (60% confidence) (UNUSED)
- Line 236: unused method 'parse_for' (60% confidence) (UNUSED)
- Line 255: unused method 'parse_if' (60% confidence) (UNUSED)
- Line 273: unused method 'parse_with' (60% confidence) (UNUSED)
- Line 290: unused method 'parse_autoescape' (60% confidence) (UNUSED)
- Line 296: unused method 'parse_block' (60% confidence) (UNUSED)
- Line 328: unused method 'parse_extends' (60% confidence) (UNUSED)
- Line 345: unused method 'parse_include' (60% confidence) (UNUSED)
- Line 357: unused method 'parse_import' (60% confidence) (UNUSED)
- Line 364: unused method 'parse_from' (60% confidence) (UNUSED)
- Line 443: unused method 'parse_macro' (60% confidence) (UNUSED)
- Line 450: unused method 'parse_print' (60% confidence) (UNUSED)

#### runtime.py
- Line 37: unused class 'LoopRenderFunc' (60% confidence) (UNUSED)
- Line 40: unused variable 'reciter' (100% confidence) (UNUSED)
- Line 41: unused variable 'loop_render_func' (100% confidence) (UNUSED)
- Line 77: unused function 'markup_join' (60% confidence) (UNUSED)
- Line 88: unused function 'str_join' (60% confidence) (UNUSED)
- Line 122: unused class 'TemplateReference' (60% confidence) (UNUSED)
- Line 466: unused property 'revindex0' (60% confidence) (UNUSED)
- Line 474: unused property 'revindex' (60% confidence) (UNUSED)
- Line 509: unused property 'previtem' (60% confidence) (UNUSED)
- Line 591: unused class 'AsyncLoopContext' (60% confidence) (UNUSED)
- Line 614: unused property 'revindex0' (60% confidence) (UNUSED)
- Line 618: unused property 'revindex' (60% confidence) (UNUSED)

#### sandbox.py
- Line 268: unused method 'call_binop' (60% confidence) (UNUSED)
- Line 279: unused method 'call_unop' (60% confidence) (UNUSED)
- Line 404: unused class 'ImmutableSandboxedEnvironment' (60% confidence) (UNUSED)

#### utils.py
- Line 164: unused function 'open_if_exists' (60% confidence) (UNUSED)
- Line 448: unused attribute '_pop' (60% confidence) (UNUSED)

#### visitor.py
- Line 12: unused class 'VisitCallable' (60% confidence) (UNUSED)
- Line 83: unused method 'visit_list' (60% confidence) (UNUSED)

#### _format.py
- Line 146: unused method 'conforms' (60% confidence) (UNUSED)
- Line 236: unused function 'is_email' (60% confidence) (UNUSED)
- Line 244: unused function 'is_ipv4' (60% confidence) (UNUSED)
- Line 270: unused function 'is_host_name' (60% confidence) (UNUSED)
- Line 288: unused function 'is_idn_host_name' (60% confidence) (UNUSED)
- Line 307: unused function 'is_uri' (60% confidence) (UNUSED)
- Line 313: unused function 'is_uri_reference' (60% confidence) (UNUSED)
- Line 327: unused function 'is_iri' (60% confidence) (UNUSED)
- Line 338: unused function 'is_iri_reference' (60% confidence) (UNUSED)
- Line 349: unused function 'is_uri' (60% confidence) (UNUSED)
- Line 355: unused function 'is_uri_reference' (60% confidence) (UNUSED)
- Line 408: unused function 'is_draft3_time' (60% confidence) (UNUSED)
- Line 418: unused function 'is_css21_color' (60% confidence) (UNUSED)
- Line 431: unused function 'is_json_pointer' (60% confidence) (UNUSED)
- Line 447: unused function 'is_relative_json_pointer' (60% confidence) (UNUSED)
- Line 482: unused function 'is_uri_template' (60% confidence) (UNUSED)
- Line 510: unused function 'is_uuid' (60% confidence) (UNUSED)

#### test_deprecations.py
- Line 286: unused class 'AnotherSubclass' (60% confidence) (UNUSED)

#### test_jsonschema_test_suite.py
- Line 126: unused variable 'TestDraft3' (60% confidence) (UNUSED)
- Line 141: unused variable 'TestDraft4' (60% confidence) (UNUSED)
- Line 160: unused variable 'TestDraft6' (60% confidence) (UNUSED)
- Line 178: unused variable 'TestDraft7' (60% confidence) (UNUSED)
- Line 198: unused variable 'TestDraft201909' (60% confidence) (UNUSED)
- Line 220: unused variable 'TestDraft201909Format' (60% confidence) (UNUSED)
- Line 235: unused variable 'TestDraft202012' (60% confidence) (UNUSED)
- Line 257: unused variable 'TestDraft202012Format' (60% confidence) (UNUSED)

#### html_re.py
- Line 40: unused variable 'HTML_OPEN_CLOSE_TAG_RE' (60% confidence) (UNUSED)

#### utils.py
- Line 134: unused function 'stripEscape' (60% confidence) (UNUSED)
- Line 154: unused function 'escapeRE' (60% confidence) (UNUSED)

#### main.py
- Line 219: unused method 'reset_rules' (60% confidence) (UNUSED)
- Line 229: unused method 'add_render_rule' (60% confidence) (UNUSED)

#### renderer.py
- Line 212: unused method 'code_inline' (60% confidence) (UNUSED)
- Line 311: unused method 'hardbreak' (60% confidence) (UNUSED)
- Line 316: unused method 'softbreak' (60% confidence) (UNUSED)

#### state_block.py
- Line 55: unused attribute 'ddIndent' (60% confidence) (UNUSED)
- Line 170: unused method 'skipChars' (60% confidence) (UNUSED)
- Line 194: unused method 'skipCharsBack' (60% confidence) (UNUSED)

#### table.py
- Line 10: unused variable 'enclosingPipesRe' (60% confidence) (UNUSED)

#### smartquotes.py
- Line 12: unused variable 'QUOTE_TEST_RE' (60% confidence) (UNUSED)

#### token.py
- Line 82: unused method 'attrIndex' (60% confidence) (UNUSED)
- Line 95: unused method 'attrPush' (60% confidence) (UNUSED)

#### tree.py
- Line 22: unused class 'SyntaxTreeNode' (60% confidence) (UNUSED)
- Line 91: unused method 'to_tokens' (60% confidence) (UNUSED)

#### utils.py
- Line 157: unused function 'read_fixture_file' (60% confidence) (UNUSED)

#### __init__.py
- Line 48: unused function 'escape_silent' (60% confidence) (UNUSED)

#### mccabe.py
- Line 139: unused variable 'visitAsyncFunctionDef' (60% confidence) (UNUSED)
- Line 141: unused method 'visitClassDef' (60% confidence) (UNUSED)
- Line 173: unused variable 'visitAsyncFor' (60% confidence) (UNUSED)
- Line 173: unused variable 'visitFor' (60% confidence) (UNUSED)
- Line 173: unused variable 'visitWhile' (60% confidence) (UNUSED)
- Line 175: unused method 'visitIf' (60% confidence) (UNUSED)
- Line 218: unused variable 'visitTry' (60% confidence) (UNUSED)
- Line 225: unused variable 'visitAsyncWith' (60% confidence) (UNUSED)
- Line 292: unused function 'get_module_complexity' (60% confidence) (UNUSED)

#### api.py
- Line 76: unused function 'run_dmypy' (60% confidence) (UNUSED)

#### build.py
- Line 181: unused variable 'is_serious' (100% confidence) (UNUSED)

#### checker.py
- Line 4069: unused variable 'index_expr' (60% confidence) (UNUSED)
- Line 4080: unused variable 'index_expr' (60% confidence) (UNUSED)

#### checkexpr.py
- Line 3209: unused variable 'original_ccaller_type' (100% confidence) (UNUSED)

#### checkstrformat.py
- Line 74: unused variable 'MatchMap' (60% confidence) (UNUSED)

#### client.py
- Line 307: unused function 'do_start' (60% confidence) (UNUSED)
- Line 329: unused function 'do_restart' (60% confidence) (UNUSED)
- Line 380: unused function 'do_run' (60% confidence) (UNUSED)
- Line 422: unused function 'do_status' (60% confidence) (UNUSED)
- Line 456: unused function 'do_kill' (60% confidence) (UNUSED)
- Line 468: unused function 'do_check' (60% confidence) (UNUSED)
- Line 478: unused function 'do_recheck' (60% confidence) (UNUSED)
- Line 509: unused function 'do_suggest' (60% confidence) (UNUSED)
- Line 531: unused function 'do_inspect' (60% confidence) (UNUSED)
- Line 603: unused function 'do_hang' (60% confidence) (UNUSED)
- Line 609: unused function 'do_daemon' (60% confidence) (UNUSED)
- Line 633: unused function 'do_help' (60% confidence) (UNUSED)

#### dmypy_server.py
- Line 67: unused attribute 'dwFlags' (60% confidence) (UNUSED)
- Line 68: unused attribute 'wShowWindow' (60% confidence) (UNUSED)
- Line 89: unused variable 'npid' (60% confidence) (UNUSED)
- Line 292: unused method 'cmd_status' (60% confidence) (UNUSED)
- Line 304: unused method 'cmd_stop' (60% confidence) (UNUSED)
- Line 356: unused method 'cmd_check' (60% confidence) (UNUSED)
- Line 366: unused method 'cmd_recheck' (60% confidence) (UNUSED)
- Line 995: unused method 'cmd_hang' (60% confidence) (UNUSED)

#### fastparse.py
- Line 1237: unused method 'visit_AnnAssign' (60% confidence) (UNUSED)
- Line 1342: unused method 'visit_TryStar' (60% confidence) (UNUSED)
- Line 1413: unused method 'visit_Pass' (60% confidence) (UNUSED)
- Line 1418: unused method 'visit_Break' (60% confidence) (UNUSED)
- Line 1423: unused method 'visit_Continue' (60% confidence) (UNUSED)
- Line 1429: unused method 'visit_NamedExpr' (60% confidence) (UNUSED)
- Line 1610: unused method 'visit_JoinedStr' (60% confidence) (UNUSED)
- Line 1632: unused method 'visit_FormattedValue' (60% confidence) (UNUSED)
- Line 1715: unused method 'visit_Match' (60% confidence) (UNUSED)
- Line 1724: unused method 'visit_MatchValue' (60% confidence) (UNUSED)
- Line 1728: unused method 'visit_MatchSingleton' (60% confidence) (UNUSED)
- Line 1732: unused method 'visit_MatchSequence' (60% confidence) (UNUSED)
- Line 1740: unused method 'visit_MatchStar' (60% confidence) (UNUSED)
- Line 1749: unused method 'visit_MatchMapping' (60% confidence) (UNUSED)
- Line 1772: unused method 'visit_MatchAs' (60% confidence) (UNUSED)
- Line 1782: unused method 'visit_MatchOr' (60% confidence) (UNUSED)
- Line 1798: unused method 'visit_TypeAlias' (60% confidence) (UNUSED)

#### ipc.py
- Line 204: unused variable 'exc_ty' (100% confidence) (UNUSED)
- Line 280: unused variable 'exc_ty' (100% confidence) (UNUSED)

#### main.py
- Line 47: unused function 'stat_proxy' (60% confidence) (UNUSED)

#### moduleinspect.py
- Line 87: unused variable 'ispkg' (60% confidence) (UNUSED)

#### nodes.py
- Line 2960: unused variable 'bad_mro' (60% confidence) (UNUSED)
- Line 3128: unused attribute 'bad_mro' (60% confidence) (UNUSED)

#### operators.py
- Line 34: unused variable 'ops_falling_back_to_cmp' (60% confidence) (UNUSED)

#### common.py
- Line 256: unused function 'add_overloaded_method_to_class' (60% confidence) (UNUSED)

#### renaming.py
- Line 196: unused method 'visit_capture_pattern' (60% confidence) (UNUSED)

#### semanal.py
- Line 2594: unused attribute 'bad_mro' (60% confidence) (UNUSED)
- Line 7228: unused method 'incomplete_feature_enabled' (60% confidence) (UNUSED)

#### semanal_shared.py
- Line 101: unused method 'incomplete_feature_enabled' (60% confidence) (UNUSED)

#### astmerge.py
- Line 254: unused method 'process_param_spec_def' (60% confidence) (UNUSED)
- Line 258: unused method 'process_type_var_tuple_def' (60% confidence) (UNUSED)

#### subexpr.py
- Line 63: unused method 'visit_unicode_expr' (60% confidence) (UNUSED)

#### stubdoc.py
- Line 82: unused method 'is_special_method' (60% confidence) (UNUSED)
- Line 103: unused method 'is_catchall_signature' (60% confidence) (UNUSED)

#### stubgen.py
- Line 217: unused attribute 'decointerpreter' (60% confidence) (UNUSED)
- Line 264: unused variable 'NOT_IN_ALL' (60% confidence) (UNUSED)

#### stubgenc.py
- Line 196: unused method '_from_sig' (60% confidence) (UNUSED)
- Line 200: unused method '_from_sigs' (60% confidence) (UNUSED)

#### stubtest.py
- Line 333: unused function 'verify_mypyfile' (60% confidence) (UNUSED)
- Line 506: unused function 'verify_typeinfo' (60% confidence) (UNUSED)
- Line 1030: unused function 'verify_funcitem' (60% confidence) (UNUSED)
- Line 1092: unused function 'verify_none' (60% confidence) (UNUSED)
- Line 1099: unused function 'verify_var' (60% confidence) (UNUSED)
- Line 1143: unused function 'verify_overloadedfuncdef' (60% confidence) (UNUSED)
- Line 1207: unused function 'verify_typevarexpr' (60% confidence) (UNUSED)
- Line 1223: unused function 'verify_paramspecexpr' (60% confidence) (UNUSED)
- Line 1341: unused function 'verify_decorator' (60% confidence) (UNUSED)
- Line 1373: unused function 'verify_typealias' (60% confidence) (UNUSED)

#### subtypes.py
- Line 84: unused variable 'TypeParameterChecker' (60% confidence) (UNUSED)

#### data.py
- Line 380: unused method 'reportinfo' (60% confidence) (UNUSED)
- Line 383: unused method 'repr_failure' (60% confidence) (UNUSED)
- Line 589: unused function 'pytest_sessionstart' (60% confidence) (UNUSED)
- Line 598: unused function 'pytest_addoption' (60% confidence) (UNUSED)
- Line 629: unused function 'pytest_cmdline_main' (60% confidence) (UNUSED)
- Line 635: unused attribute 'numprocesses' (60% confidence) (UNUSED)
- Line 640: unused function 'pytest_pycollect_makeitem' (60% confidence) (UNUSED)
- Line 794: unused function 'is_incremental' (60% confidence) (UNUSED)
- Line 798: unused function 'has_stable_flags' (60% confidence) (UNUSED)

#### helpers.py
- Line 38: unused function 'run_mypy' (60% confidence) (UNUSED)

#### test_diff_helper.py
- Line 6: unused class 'DiffHelperSuite' (60% confidence) (UNUSED)

#### test_update_data.py
- Line 19: unused class 'UpdateDataSuite' (60% confidence) (UNUSED)

#### test_config_parser.py
- Line 36: unused class 'FindConfigFileSuite' (60% confidence) (UNUSED)

#### test_find_sources.py
- Line 66: unused class 'SourceFinderSuite' (60% confidence) (UNUSED)

#### test_ref_info.py
- Line 17: unused class 'RefInfoSuite' (60% confidence) (UNUSED)

#### testapi.py
- Line 10: unused class 'APISuite' (60% confidence) (UNUSED)

#### testargs.py
- Line 18: unused class 'ArgSuite' (60% confidence) (UNUSED)

#### testcheck.py
- Line 54: unused class 'TypeCheckSuite' (60% confidence) (UNUSED)

#### testcmdline.py
- Line 36: unused class 'PythonCmdlineSuite' (60% confidence) (UNUSED)

#### testconstraints.py
- Line 9: unused class 'ConstraintsSuite' (60% confidence) (UNUSED)

#### testdaemon.py
- Line 27: unused class 'DaemonSuite' (60% confidence) (UNUSED)
- Line 97: unused class 'DaemonUtilitySuite' (60% confidence) (UNUSED)

#### testdeps.py
- Line 27: unused class 'GetDependenciesSuite' (60% confidence) (UNUSED)

#### testdiff.py
- Line 21: unused class 'ASTDiffSuite' (60% confidence) (UNUSED)

#### testerrorstream.py
- Line 13: unused class 'ErrorStreamSuite' (60% confidence) (UNUSED)

#### testfinegrainedcache.py
- Line 13: unused class 'FineGrainedCacheSuite' (60% confidence) (UNUSED)

#### testgraph.py
- Line 20: unused class 'GraphSuite' (60% confidence) (UNUSED)

#### testinfer.py
- Line 14: unused class 'MapActualsToFormalsSuite' (60% confidence) (UNUSED)
- Line 151: unused class 'OperandDisjointDictSuite' (60% confidence) (UNUSED)
- Line 209: unused class 'OperandComparisonGroupingSuite' (60% confidence) (UNUSED)

#### testmerge.py
- Line 40: unused class 'ASTMergeSuite' (60% confidence) (UNUSED)

#### testmodulefinder.py
- Line 13: unused class 'ModuleFinderSuite' (60% confidence) (UNUSED)
- Line 140: unused class 'ModuleFinderSitePackagesSuite' (60% confidence) (UNUSED)

#### testoutput.py
- Line 18: unused class 'OutputJSONsuite' (60% confidence) (UNUSED)

#### testparse.py
- Line 19: unused class 'ParserSuite' (60% confidence) (UNUSED)
- Line 82: unused class 'ParseErrorSuite' (60% confidence) (UNUSED)

#### testpep561.py
- Line 22: unused class 'PEP561Suite' (60% confidence) (UNUSED)

#### testpythoneval.py
- Line 33: unused class 'PythonEvaluationSuite' (60% confidence) (UNUSED)

#### testreports.py
- Line 18: unused class 'CoberturaReportSuite' (60% confidence) (UNUSED)

#### testsemanal.py
- Line 51: unused class 'SemAnalSuite' (60% confidence) (UNUSED)
- Line 95: unused class 'SemAnalErrorSuite' (60% confidence) (UNUSED)
- Line 129: unused class 'SemAnalSymtableSuite' (60% confidence) (UNUSED)
- Line 162: unused class 'SemAnalTypeInfoSuite' (60% confidence) (UNUSED)

#### testsolve.py
- Line 12: unused class 'SolveSuite' (60% confidence) (UNUSED)

#### teststubgen.py
- Line 51: unused class 'StubgenCmdLineSuite' (60% confidence) (UNUSED)
- Line 133: unused class 'StubgenCliParseSuite' (60% confidence) (UNUSED)
- Line 151: unused class 'StubgenUtilSuite' (60% confidence) (UNUSED)
- Line 627: unused class 'StubgenHelpersSuite' (60% confidence) (UNUSED)
- Line 668: unused class 'StubgenPythonSuite' (60% confidence) (UNUSED)
- Line 796: unused class 'StubgencSuite' (60% confidence) (UNUSED)
- Line 862: unused variable 'keyword_only' (100% confidence) (UNUSED)
- Line 862: unused variable 'keyword_only_with_default' (100% confidence) (UNUSED)
- Line 1376: unused class 'ArgSigSuite' (60% confidence) (UNUSED)
- Line 1391: unused class 'IsValidTypeSuite' (60% confidence) (UNUSED)
- Line 1419: unused class 'ModuleInspectSuite' (60% confidence) (UNUSED)

#### teststubtest.py
- Line 238: unused class 'StubtestUnit' (60% confidence) (UNUSED)
- Line 2431: unused class 'StubtestMiscUnit' (60% confidence) (UNUSED)

#### testsubtypes.py
- Line 10: unused class 'SubtypingSuite' (60% confidence) (UNUSED)

#### testtransform.py
- Line 14: unused class 'TransformSuite' (60% confidence) (UNUSED)

#### testtypegen.py
- Line 19: unused class 'TypeExportSuite' (60% confidence) (UNUSED)

#### testtypes.py
- Line 59: unused class 'TypesSuite' (60% confidence) (UNUSED)
- Line 244: unused class 'TypeOpsSuite' (60% confidence) (UNUSED)
- Line 695: unused class 'JoinSuite' (60% confidence) (UNUSED)
- Line 1106: unused class 'MeetSuite' (60% confidence) (UNUSED)
- Line 1367: unused class 'SameTypeSuite' (60% confidence) (UNUSED)
- Line 1410: unused class 'RemoveLastKnownValueSuite' (60% confidence) (UNUSED)
- Line 1452: unused class 'ShallowOverloadMatchingSuite' (60% confidence) (UNUSED)

#### typefixture.py
- Line 74: unused attribute 'sf1' (60% confidence) (UNUSED)
- Line 168: unused attribute 'gtf' (60% confidence) (UNUSED)
- Line 169: unused attribute 'gtf2' (60% confidence) (UNUSED)
- Line 172: unused attribute 'gn' (60% confidence) (UNUSED)
- Line 181: unused attribute 'gs2b' (60% confidence) (UNUSED)
- Line 187: unused attribute 'hts' (60% confidence) (UNUSED)
- Line 191: unused attribute 'lsta' (60% confidence) (UNUSED)
- Line 192: unused attribute 'lstb' (60% confidence) (UNUSED)

#### traverser.py
- Line 948: unused class 'YieldFromCollector' (60% confidence) (UNUSED)

#### typeanal.py
- Line 2015: unused variable '__ctx' (100% confidence) (UNUSED)

#### util.py
- Line 243: unused variable 'JUNIT_ERROR_TEMPLATE' (60% confidence) (UNUSED)

#### mypy_extensions.py
- Line 122: unused function 'Arg' (60% confidence) (UNUSED)
- Line 127: unused function 'DefaultArg' (60% confidence) (UNUSED)
- Line 132: unused function 'NamedArg' (60% confidence) (UNUSED)
- Line 137: unused function 'DefaultNamedArg' (60% confidence) (UNUSED)
- Line 142: unused function 'VarArg' (60% confidence) (UNUSED)
- Line 147: unused function 'KwArg' (60% confidence) (UNUSED)
- Line 154: unused class '_DEPRECATED_NoReturn' (60% confidence) (UNUSED)
- Line 161: unused variable 'kwattrs' (100% confidence) (UNUSED)

#### dataflow.py
- Line 417: unused class 'UndefinedVisitor' (60% confidence) (UNUSED)

#### build.py
- Line 461: unused function 'mypycify' (60% confidence) (UNUSED)

#### emit.py
- Line 243: unused method 'emit_printf' (60% confidence) (UNUSED)

#### emitfunc.py
- Line 831: unused method 'emit_declaration' (60% confidence) (UNUSED)

#### emitmodule.py
- Line 1064: unused method 'declare_static_pyobject' (60% confidence) (UNUSED)
- Line 1081: unused function 'toposort' (60% confidence) (UNUSED)

#### errors.py
- Line 10: unused attribute 'num_warnings' (60% confidence) (UNUSED)
- Line 22: unused attribute 'num_warnings' (60% confidence) (UNUSED)

#### class_ir.py
- Line 213: unused method 'real_base' (60% confidence) (UNUSED)
- Line 305: unused method 'has_method_decl' (60% confidence) (UNUSED)

#### rtypes.py
- Line 338: unused variable 'u16_rprimitive' (60% confidence) (UNUSED)
- Line 501: unused function 'is_uint32_rprimitive' (60% confidence) (UNUSED)
- Line 505: unused function 'is_uint64_rprimitive' (60% confidence) (UNUSED)
- Line 509: unused function 'is_c_py_ssize_t_rprimitive' (60% confidence) (UNUSED)

#### builder.py
- Line 780: unused method 'process_iterator_tuple_assignment_helper' (60% confidence) (UNUSED)

#### function.py
- Line 840: unused variable 'main_singledispatch_function_name' (100% confidence) (UNUSED)

#### specialize.py
- Line 164: unused function 'translate_globals' (60% confidence) (UNUSED)
- Line 171: unused function 'translate_builtins_with_unary_dunder' (60% confidence) (UNUSED)
- Line 201: unused function 'translate_len' (60% confidence) (UNUSED)
- Line 221: unused function 'dict_methods_fast_path' (60% confidence) (UNUSED)
- Line 252: unused function 'translate_list_from_generator_call' (60% confidence) (UNUSED)
- Line 277: unused function 'translate_tuple_from_generator_call' (60% confidence) (UNUSED)
- Line 302: unused function 'translate_set_from_generator_call' (60% confidence) (UNUSED)
- Line 320: unused function 'faster_min_max' (60% confidence) (UNUSED)
- Line 348: unused function 'translate_safe_generator_call' (60% confidence) (UNUSED)
- Line 395: unused function 'translate_any_call' (60% confidence) (UNUSED)
- Line 406: unused function 'translate_all_call' (60% confidence) (UNUSED)
- Line 449: unused function 'translate_sum_call' (60% confidence) (UNUSED)
- Line 488: unused function 'translate_dataclasses_field_call' (60% confidence) (UNUSED)
- Line 505: unused function 'translate_next_call' (60% confidence) (UNUSED)
- Line 549: unused function 'translate_isinstance' (60% confidence) (UNUSED)
- Line 575: unused function 'translate_dict_setdefault' (60% confidence) (UNUSED)
- Line 621: unused function 'translate_str_format' (60% confidence) (UNUSED)
- Line 641: unused function 'translate_fstring' (60% confidence) (UNUSED)
- Line 691: unused function 'str_encode_fast_path' (60% confidence) (UNUSED)
- Line 743: unused function 'translate_i64' (60% confidence) (UNUSED)
- Line 763: unused function 'translate_i32' (60% confidence) (UNUSED)
- Line 787: unused function 'translate_i16' (60% confidence) (UNUSED)
- Line 808: unused function 'translate_u8' (60% confidence) (UNUSED)
- Line 846: unused function 'translate_int' (60% confidence) (UNUSED)
- Line 862: unused function 'translate_bool' (60% confidence) (UNUSED)
- Line 871: unused function 'translate_float' (60% confidence) (UNUSED)
- Line 883: unused function 'translate_ord' (60% confidence) (UNUSED)

#### visitor.py
- Line 398: unused method 'bail' (60% confidence) (UNUSED)

#### int_ops.py
- Line 23: unused variable 'binary_op_variant' (60% confidence) (UNUSED)
- Line 24: unused variable 'c_func_description' (60% confidence) (UNUSED)
- Line 25: unused variable 'c_func_negated' (60% confidence) (UNUSED)
- Line 26: unused variable 'c_func_swap_operands' (60% confidence) (UNUSED)
- Line 86: unused function 'lower_int_eq' (60% confidence) (UNUSED)
- Line 91: unused function 'lower_int_ne' (60% confidence) (UNUSED)
- Line 96: unused function 'lower_int_lt' (60% confidence) (UNUSED)
- Line 101: unused function 'lower_int_le' (60% confidence) (UNUSED)
- Line 106: unused function 'lower_int_gt' (60% confidence) (UNUSED)
- Line 111: unused function 'lower_int_ge' (60% confidence) (UNUSED)

#### list_ops.py
- Line 67: unused function 'list_get_item_unsafe' (60% confidence) (UNUSED)

#### dict_ops.py
- Line 150: unused variable 'dict_setdefault_op' (60% confidence) (UNUSED)

#### float_ops.py
- Line 135: unused variable 'pow_op' (60% confidence) (UNUSED)

#### int_ops.py
- Line 113: unused variable 'int_eq' (60% confidence) (UNUSED)
- Line 114: unused variable 'int_ne' (60% confidence) (UNUSED)
- Line 115: unused variable 'int_lt' (60% confidence) (UNUSED)
- Line 116: unused variable 'int_le' (60% confidence) (UNUSED)
- Line 117: unused variable 'int_gt' (60% confidence) (UNUSED)
- Line 118: unused variable 'int_ge' (60% confidence) (UNUSED)
- Line 183: unused variable 'int_invert_op' (60% confidence) (UNUSED)

#### list_ops.py
- Line 203: unused variable 'list_pop' (60% confidence) (UNUSED)

#### tuple_ops.py
- Line 24: unused variable 'tuple_get_item_op' (60% confidence) (UNUSED)

#### test_analysis.py
- Line 30: unused variable 'optional_out' (60% confidence) (UNUSED)

#### test_commandline.py
- Line 31: unused variable 'optional_out' (60% confidence) (UNUSED)

#### test_irbuild.py
- Line 64: unused variable 'optional_out' (60% confidence) (UNUSED)

#### test_refcount.py
- Line 35: unused variable 'optional_out' (60% confidence) (UNUSED)

#### test_run.py
- Line 143: unused variable 'optional_out' (60% confidence) (UNUSED)

#### testutil.py
- Line 41: unused function 'builtins_wrapper' (60% confidence) (UNUSED)
- Line 189: unused function 'get_func_names' (60% confidence) (UNUSED)

#### dataframe.py
- Line 81: unused variable 'PromoteOptions' (60% confidence) (UNUSED)

#### group_by.py
- Line 61: unused attribute '_drop_null_keys' (60% confidence) (UNUSED)

#### typing.py
- Line 20: unused import 'Indices' (90% confidence) (UNUSED)
- Line 33: unused variable 'IntoArrowExpr' (60% confidence) (UNUSED)

#### typing.py
- Line 50: unused variable 'EagerDataFrameAny' (60% confidence) (UNUSED)
- Line 63: unused variable 'NativeFrameT_contra' (60% confidence) (UNUSED)
- Line 93: unused variable 'CompliantLazyFrameT_co' (60% confidence) (UNUSED)
- Line 96: unused variable 'CompliantNamespaceT' (60% confidence) (UNUSED)

#### _enum.py
- Line 34: unused method '_generate_next_value_' (60% confidence) (UNUSED)
- Line 36: unused variable 'last_values' (100% confidence) (UNUSED)

#### _namespace.py
- Line 86: unused variable 'EagerOnly' (60% confidence) (UNUSED)
- Line 88: unused variable 'LazyOnly' (60% confidence) (UNUSED)
- Line 89: unused variable 'LazyAllowed' (60% confidence) (UNUSED)
- Line 91: unused variable 'BackendName' (60% confidence) (UNUSED)
- Line 107: unused method 'to_pylibcudf' (60% confidence) (UNUSED)
- Line 115: unused class '_ModinDataFrame' (60% confidence) (UNUSED)
- Line 118: unused class '_ModinSeries' (60% confidence) (UNUSED)
- Line 134: unused variable 'NativeKnown' (60% confidence) (UNUSED)

#### group_by.py
- Line 47: unused attribute '_drop_null_keys' (60% confidence) (UNUSED)

#### typing.py
- Line 15: unused variable 'IntoPandasLikeExpr' (60% confidence) (UNUSED)

#### utils.py
- Line 39: unused variable 'PANDAS_LIKE_IMPLEMENTATION' (60% confidence) (UNUSED)

#### typing.py
- Line 20: unused variable 'IntoPolarsExpr' (60% confidence) (UNUSED)

#### dataframe.py
- Line 70: unused import '_MultiColSelector' (90% confidence) (UNUSED)
- Line 71: unused import '_MultiIndexSelector' (90% confidence) (UNUSED)

#### dependencies.py
- Line 317: unused function 'is_pandas_like_index' (60% confidence) (UNUSED)

#### dtypes.py
- Line 599: unused method 'to_schema' (60% confidence) (UNUSED)

#### exceptions.py
- Line 92: unused method 'from_expr_name' (60% confidence) (UNUSED)

#### typing.py
- Line 134: unused variable 'IntoLazyFrame' (60% confidence) (UNUSED)
- Line 383: unused variable 'SingleNameSelector' (60% confidence) (UNUSED)
- Line 386: unused variable 'MultiNameSelector' (60% confidence) (UNUSED)

#### utils.py
- Line 122: unused class '_SupportsGet' (60% confidence) (UNUSED)
- Line 1224: unused function 'generate_unique_token' (60% confidence) (UNUSED)

#### __init__.py
- Line 541: unused function '_pyinstaller_hooks_dir' (60% confidence) (UNUSED)

#### _dtype.py
- Line 350: unused function '_name_get' (60% confidence) (UNUSED)

#### _exceptions.py
- Line 56: unused class '_UFuncBinaryResolutionError' (60% confidence) (UNUSED)
- Line 80: unused class '_UFuncInputCastingError' (60% confidence) (UNUSED)
- Line 98: unused class '_UFuncOutputCastingError' (60% confidence) (UNUSED)

#### _internal.py
- Line 58: unused function '_usefields' (60% confidence) (UNUSED)
- Line 151: unused function '_commastring' (60% confidence) (UNUSED)
- Line 408: unused function '_newnames' (60% confidence) (UNUSED)
- Line 431: unused function '_copy_fields' (60% confidence) (UNUSED)
- Line 449: unused function '_promote_fields' (60% confidence) (UNUSED)
- Line 506: unused function '_getfield_is_safe' (60% confidence) (UNUSED)
- Line 538: unused function '_view_is_safe' (60% confidence) (UNUSED)
- Line 874: unused function 'array_ufunc_errmsg_formatter' (60% confidence) (UNUSED)
- Line 886: unused function 'array_function_errmsg_formatter' (60% confidence) (UNUSED)
- Line 893: unused function '_ufunc_doc_signature_formatter' (60% confidence) (UNUSED)
- Line 941: unused function 'npy_ctypes_check' (60% confidence) (UNUSED)
- Line 960: unused function '_convert_to_stringdtype_kwargs' (60% confidence) (UNUSED)

#### _methods.py
- Line 42: unused function '_amax' (60% confidence) (UNUSED)
- Line 46: unused function '_amin' (60% confidence) (UNUSED)
- Line 50: unused function '_sum' (60% confidence) (UNUSED)
- Line 250: unused method '_dumps' (60% confidence) (UNUSED)
- Line 253: unused function '_bitwise_count' (60% confidence) (UNUSED)

#### _string_helpers.py
- Line 16: unused function 'english_lower' (60% confidence) (UNUSED)
- Line 72: unused function 'english_capitalize' (60% confidence) (UNUSED)

#### arrayprint.py
- Line 984: unused attribute 'large_exponent' (60% confidence) (UNUSED)
- Line 1469: unused function '_void_scalar_to_string' (60% confidence) (UNUSED)

#### getlimits.py
- Line 566: unused attribute '_str_tiny' (60% confidence) (UNUSED)
- Line 567: unused attribute '_str_max' (60% confidence) (UNUSED)

#### memmap.py
- Line 11: unused variable 'writeable_filemodes' (60% confidence) (UNUSED)

#### multiarray.py
- Line 16: unused import '_get_madvise_hugepage' (90% confidence) (UNUSED)
- Line 1332: unused variable 'max_work' (100% confidence) (UNUSED)
- Line 1411: unused variable 'max_work' (100% confidence) (UNUSED)
- Line 1453: unused variable 'busdaycal' (100% confidence) (UNUSED)
- Line 1513: unused variable 'busdaycal' (100% confidence) (UNUSED)
- Line 1615: unused variable 'busdaycal' (100% confidence) (UNUSED)

#### numeric.py
- Line 284: unused function '_full_dispatcher' (60% confidence) (UNUSED)
- Line 1923: unused function '_frombuffer' (60% confidence) (UNUSED)

#### numerictypes.py
- Line 115: unused variable 'genericTypeRank' (60% confidence) (UNUSED)
- Line 331: unused function 'issubsctype' (60% confidence) (UNUSED)
- Line 620: unused variable 'typeDict' (60% confidence) (UNUSED)

#### records.py
- Line 43: unused variable 'numfmt' (60% confidence) (UNUSED)

#### test_array_coercion.py
- Line 140: unused function 'is_parametric_dtype' (60% confidence) (UNUSED)

#### test_custom_dtypes.py
- Line 257: unused attribute '_ScaledFloatTestDType' (60% confidence) (UNUSED)
- Line 301: unused attribute '_ScaledFloatTestDType' (60% confidence) (UNUSED)

#### test_cython.py
- Line 35: unused function 'install_temp' (60% confidence) (UNUSED)
- Line 82: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 95: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 107: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 118: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 129: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 143: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 150: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 156: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 162: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 184: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 192: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 209: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 224: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 230: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 242: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 286: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 293: unused variable 'install_temp' (100% confidence) (UNUSED)

#### test_deprecations.py
- Line 323: unused class 'BuiltInRoundComplexDType' (60% confidence) (UNUSED)
- Line 398: unused class 'FlatteningConcatenateUnsafeCast' (60% confidence) (UNUSED)

#### test_indexing.py
- Line 917: unused variable 'fancy_dim' (60% confidence) (UNUSED)
- Line 937: unused variable 'fancy_dim' (60% confidence) (UNUSED)
- Line 964: unused variable 'fancy_dim' (60% confidence) (UNUSED)

#### test_limited_api.py
- Line 34: unused function 'install_temp' (60% confidence) (UNUSED)
- Line 93: unused variable 'install_temp' (100% confidence) (UNUSED)
- Line 98: unused import 'limited_api1' (90% confidence) (UNUSED)
- Line 99: unused import 'limited_api_latest' (90% confidence) (UNUSED)
- Line 100: unused import 'limited_api2' (90% confidence) (UNUSED)

#### test_multiarray.py
- Line 219: unused attribute '_warn_on_write' (60% confidence) (UNUSED)
- Line 5660: unused method 'decimal_sep_localization' (60% confidence) (UNUSED)
- Line 5688: unused variable 'decimal_sep_localization' (100% confidence) (UNUSED)
- Line 5695: unused variable 'decimal_sep_localization' (100% confidence) (UNUSED)
- Line 5702: unused variable 'decimal_sep_localization' (100% confidence) (UNUSED)
- Line 5719: unused variable 'decimal_sep_localization' (100% confidence) (UNUSED)
- Line 5736: unused variable 'decimal_sep_localization' (100% confidence) (UNUSED)
- Line 5742: unused variable 'decimal_sep_localization' (100% confidence) (UNUSED)
- Line 5765: unused variable 'decimal_sep_localization' (100% confidence) (UNUSED)
- Line 5775: unused variable 'decimal_sep_localization' (100% confidence) (UNUSED)

#### test_nditer.py
- Line 2354: unused variable 'b2_in' (60% confidence) (UNUSED)
- Line 2355: unused variable 'b2_in' (60% confidence) (UNUSED)
- Line 2368: unused variable 'b1_in' (60% confidence) (UNUSED)
- Line 2369: unused variable 'b1_in' (60% confidence) (UNUSED)
- Line 2791: unused function '_is_buffered' (60% confidence) (UNUSED)

#### test_numeric.py
- Line 970: unused method 'assert_op_raises_fpe' (60% confidence) (UNUSED)
- Line 2096: unused variable 'aS1u4b' (60% confidence) (UNUSED)
- Line 2313: unused method '_generate_flt_data' (60% confidence) (UNUSED)

#### test_records.py
- Line 380: unused attribute 'col5' (60% confidence) (UNUSED)

#### test_scalarprint.py
- Line 412: unused method 'float32_roundtrip' (60% confidence) (UNUSED)
- Line 420: unused method 'float64_vs_python' (60% confidence) (UNUSED)

#### test_stringdtype.py
- Line 568: unused variable 'sarr_cat' (60% confidence) (UNUSED)
- Line 1396: unused variable 'unicode_bug_fail' (60% confidence) (UNUSED)

#### test_umath.py
- Line 498: unused variable 'lsize' (60% confidence) (UNUSED)
- Line 956: unused variable 'operand_identifier' (60% confidence) (UNUSED)
- Line 985: unused variable 'operand_identifier' (60% confidence) (UNUSED)
- Line 2227: unused function 'assert_arctan2_ispinf' (60% confidence) (UNUSED)
- Line 2231: unused function 'assert_arctan2_isninf' (60% confidence) (UNUSED)

#### umath.py
- Line 15: unused import '_ones_like' (90% confidence) (UNUSED)
- Line 15: unused import '_UFUNC_API' (90% confidence) (UNUSED)

#### _distributor_init.py
- Line 13: unused import '_distributor_init_local' (90% confidence) (UNUSED)

#### hook-numpy.py
- Line 8: unused import 'is_conda' (90% confidence) (UNUSED)
- Line 9: unused import 'is_module_satisfies' (90% confidence) (UNUSED)
- Line 13: unused variable 'binaries' (60% confidence) (UNUSED)
- Line 25: unused variable 'hiddenimports' (60% confidence) (UNUSED)
- Line 29: unused variable 'excludedimports' (60% confidence) (UNUSED)

#### _array_like.py
- Line 95: unused function '__buffer__' (60% confidence) (UNUSED)

#### _extended_precision.py
- Line 16: unused variable 'uint128' (60% confidence) (UNUSED)
- Line 17: unused variable 'uint256' (60% confidence) (UNUSED)
- Line 18: unused variable 'int128' (60% confidence) (UNUSED)
- Line 19: unused variable 'int256' (60% confidence) (UNUSED)
- Line 20: unused variable 'float80' (60% confidence) (UNUSED)
- Line 23: unused variable 'float256' (60% confidence) (UNUSED)
- Line 24: unused variable 'complex160' (60% confidence) (UNUSED)
- Line 25: unused variable 'complex192' (60% confidence) (UNUSED)
- Line 27: unused variable 'complex512' (60% confidence) (UNUSED)

#### _inspect.py
- Line 63: unused variable 'CO_NEWLOCALS' (60% confidence) (UNUSED)
- Line 63: unused variable 'CO_OPTIMIZED' (60% confidence) (UNUSED)
- Line 113: unused function 'getargvalues' (60% confidence) (UNUSED)
- Line 168: unused function 'formatargvalues' (60% confidence) (UNUSED)

#### conftest.py
- Line 59: unused function 'pytest_configure' (60% confidence) (UNUSED)
- Line 70: unused function 'pytest_addoption' (60% confidence) (UNUSED)
- Line 85: unused function 'pytest_sessionstart' (60% confidence) (UNUSED)
- Line 91: unused function 'pytest_terminal_summary' (60% confidence) (UNUSED)
- Line 106: unused function 'pytest_itemcollected' (60% confidence) (UNUSED)
- Line 126: unused function 'check_fpu_mode' (60% confidence) (UNUSED)
- Line 147: unused function 'add_np' (60% confidence) (UNUSED)
- Line 151: unused function 'env_setup' (60% confidence) (UNUSED)
- Line 194: unused attribute 'user_context_mgr' (60% confidence) (UNUSED)
- Line 201: unused attribute 'strict_check' (60% confidence) (UNUSED)
- Line 204: unused attribute 'optionflags' (60% confidence) (UNUSED)
- Line 210: unused attribute 'skiplist' (60% confidence) (UNUSED)
- Line 218: unused attribute 'pytest_extra_xfail' (60% confidence) (UNUSED)
- Line 228: unused attribute 'pytest_extra_ignore' (60% confidence) (UNUSED)

#### __init__.py
- Line 13: unused function '_ufunc_reconstruct' (60% confidence) (UNUSED)

#### ctypeslib.py
- Line 207: unused method '_check_retval_' (60% confidence) (UNUSED)
- Line 601: unused attribute '__keep' (60% confidence) (UNUSED)

#### _shell_utils.py
- Line 12: unused class 'CommandLineParser' (60% confidence) (UNUSED)

#### armccompiler.py
- Line 3: unused class 'ArmCCompiler' (60% confidence) (UNUSED)

#### __init__.py
- Line 7: unused function 'test_na_writable_attributes_deletion' (60% confidence) (UNUSED)

#### build_ext.py
- Line 630: unused method '_add_dummy_mingwex_sym' (60% confidence) (UNUSED)

#### config.py
- Line 166: unused method 'check_header' (60% confidence) (UNUSED)
- Line 172: unused method 'check_decl' (60% confidence) (UNUSED)
- Line 187: unused method 'check_macro_true' (60% confidence) (UNUSED)
- Line 232: unused method 'check_type_size' (60% confidence) (UNUSED)
- Line 349: unused method 'check_funcs_once' (60% confidence) (UNUSED)

#### config_compiler.py
- Line 49: unused attribute 'f77exec' (60% confidence) (UNUSED)
- Line 50: unused attribute 'f90exec' (60% confidence) (UNUSED)

#### cpuinfo.py
- Line 85: unused method '_getNCPUs' (60% confidence) (UNUSED)
- Line 93: unused method '_is_32bit' (60% confidence) (UNUSED)
- Line 96: unused method '_is_64bit' (60% confidence) (UNUSED)
- Line 133: unused method '_is_AthlonK6_2' (60% confidence) (UNUSED)
- Line 136: unused method '_is_AthlonK6_3' (60% confidence) (UNUSED)
- Line 139: unused method '_is_AthlonK6' (60% confidence) (UNUSED)
- Line 142: unused method '_is_AthlonK7' (60% confidence) (UNUSED)
- Line 145: unused method '_is_AthlonMP' (60% confidence) (UNUSED)
- Line 149: unused method '_is_AMD64' (60% confidence) (UNUSED)
- Line 152: unused method '_is_Athlon64' (60% confidence) (UNUSED)
- Line 156: unused method '_is_AthlonHX' (60% confidence) (UNUSED)
- Line 160: unused method '_is_Opteron' (60% confidence) (UNUSED)
- Line 164: unused method '_is_Hammer' (60% confidence) (UNUSED)
- Line 170: unused method '_is_Alpha' (60% confidence) (UNUSED)
- Line 173: unused method '_is_EV4' (60% confidence) (UNUSED)
- Line 176: unused method '_is_EV5' (60% confidence) (UNUSED)
- Line 179: unused method '_is_EV56' (60% confidence) (UNUSED)
- Line 182: unused method '_is_PCA56' (60% confidence) (UNUSED)
- Line 190: unused method '_is_Intel' (60% confidence) (UNUSED)
- Line 193: unused method '_is_i486' (60% confidence) (UNUSED)
- Line 196: unused method '_is_i586' (60% confidence) (UNUSED)
- Line 199: unused method '_is_i686' (60% confidence) (UNUSED)
- Line 202: unused method '_is_Celeron' (60% confidence) (UNUSED)
- Line 206: unused method '_is_Pentium' (60% confidence) (UNUSED)
- Line 210: unused method '_is_PentiumII' (60% confidence) (UNUSED)
- Line 214: unused method '_is_PentiumPro' (60% confidence) (UNUSED)
- Line 218: unused method '_is_PentiumMMX' (60% confidence) (UNUSED)
- Line 222: unused method '_is_PentiumIII' (60% confidence) (UNUSED)
- Line 226: unused method '_is_PentiumIV' (60% confidence) (UNUSED)
- Line 230: unused method '_is_PentiumM' (60% confidence) (UNUSED)
- Line 234: unused method '_is_Prescott' (60% confidence) (UNUSED)
- Line 237: unused method '_is_Nocona' (60% confidence) (UNUSED)
- Line 244: unused method '_is_Core2' (60% confidence) (UNUSED)
- Line 249: unused method '_is_Itanium' (60% confidence) (UNUSED)
- Line 261: unused method '_is_singleCPU' (60% confidence) (UNUSED)
- Line 264: unused method '_getNCPUs' (60% confidence) (UNUSED)
- Line 267: unused method '_has_fdiv_bug' (60% confidence) (UNUSED)
- Line 270: unused method '_has_f00f_bug' (60% confidence) (UNUSED)
- Line 273: unused method '_has_mmx' (60% confidence) (UNUSED)
- Line 276: unused method '_has_sse' (60% confidence) (UNUSED)
- Line 279: unused method '_has_sse2' (60% confidence) (UNUSED)
- Line 282: unused method '_has_sse3' (60% confidence) (UNUSED)
- Line 285: unused method '_has_ssse3' (60% confidence) (UNUSED)
- Line 288: unused method '_has_3dnow' (60% confidence) (UNUSED)
- Line 291: unused method '_has_3dnowext' (60% confidence) (UNUSED)
- Line 306: unused method '_is_singleCPU' (60% confidence) (UNUSED)
- Line 309: unused method '_getNCPUs' (60% confidence) (UNUSED)
- Line 314: unused method '_is_r2000' (60% confidence) (UNUSED)
- Line 315: unused method '_is_r3000' (60% confidence) (UNUSED)
- Line 316: unused method '_is_r3900' (60% confidence) (UNUSED)
- Line 318: unused method '_is_r4100' (60% confidence) (UNUSED)
- Line 319: unused method '_is_r4300' (60% confidence) (UNUSED)
- Line 320: unused method '_is_r4400' (60% confidence) (UNUSED)
- Line 321: unused method '_is_r4600' (60% confidence) (UNUSED)
- Line 322: unused method '_is_r4650' (60% confidence) (UNUSED)
- Line 324: unused method '_is_r6000' (60% confidence) (UNUSED)
- Line 325: unused method '_is_r8000' (60% confidence) (UNUSED)
- Line 327: unused method '_is_r12000' (60% confidence) (UNUSED)
- Line 328: unused method '_is_rorion' (60% confidence) (UNUSED)
- Line 330: unused method 'get_ip' (60% confidence) (UNUSED)
- Line 335: unused method '_is_IP19' (60% confidence) (UNUSED)
- Line 336: unused method '_is_IP20' (60% confidence) (UNUSED)
- Line 337: unused method '_is_IP21' (60% confidence) (UNUSED)
- Line 338: unused method '_is_IP22' (60% confidence) (UNUSED)
- Line 339: unused method '_is_IP22_4k' (60% confidence) (UNUSED)
- Line 340: unused method '_is_IP22_5k' (60% confidence) (UNUSED)
- Line 341: unused method '_is_IP24' (60% confidence) (UNUSED)
- Line 342: unused method '_is_IP25' (60% confidence) (UNUSED)
- Line 343: unused method '_is_IP26' (60% confidence) (UNUSED)
- Line 344: unused method '_is_IP27' (60% confidence) (UNUSED)
- Line 345: unused method '_is_IP28' (60% confidence) (UNUSED)
- Line 346: unused method '_is_IP30' (60% confidence) (UNUSED)
- Line 347: unused method '_is_IP32' (60% confidence) (UNUSED)
- Line 348: unused method '_is_IP32_5k' (60% confidence) (UNUSED)
- Line 349: unused method '_is_IP32_10k' (60% confidence) (UNUSED)
- Line 365: unused method '_getNCPUs' (60% confidence) (UNUSED)
- Line 368: unused method '_is_Power_Macintosh' (60% confidence) (UNUSED)
- Line 371: unused method '_is_i386' (60% confidence) (UNUSED)
- Line 373: unused method '_is_ppc' (60% confidence) (UNUSED)
- Line 378: unused method '_is_ppc601' (60% confidence) (UNUSED)
- Line 379: unused method '_is_ppc602' (60% confidence) (UNUSED)
- Line 380: unused method '_is_ppc603' (60% confidence) (UNUSED)
- Line 381: unused method '_is_ppc603e' (60% confidence) (UNUSED)
- Line 382: unused method '_is_ppc604' (60% confidence) (UNUSED)
- Line 383: unused method '_is_ppc604e' (60% confidence) (UNUSED)
- Line 384: unused method '_is_ppc620' (60% confidence) (UNUSED)
- Line 385: unused method '_is_ppc630' (60% confidence) (UNUSED)
- Line 386: unused method '_is_ppc740' (60% confidence) (UNUSED)
- Line 387: unused method '_is_ppc7400' (60% confidence) (UNUSED)
- Line 388: unused method '_is_ppc7450' (60% confidence) (UNUSED)
- Line 389: unused method '_is_ppc750' (60% confidence) (UNUSED)
- Line 390: unused method '_is_ppc403' (60% confidence) (UNUSED)
- Line 391: unused method '_is_ppc505' (60% confidence) (UNUSED)
- Line 392: unused method '_is_ppc801' (60% confidence) (UNUSED)
- Line 393: unused method '_is_ppc821' (60% confidence) (UNUSED)
- Line 394: unused method '_is_ppc823' (60% confidence) (UNUSED)
- Line 395: unused method '_is_ppc860' (60% confidence) (UNUSED)
- Line 421: unused method '_is_i386' (60% confidence) (UNUSED)
- Line 423: unused method '_is_sparc' (60% confidence) (UNUSED)
- Line 425: unused method '_is_sparcv9' (60% confidence) (UNUSED)
- Line 428: unused method '_getNCPUs' (60% confidence) (UNUSED)
- Line 431: unused method '_is_sun4' (60% confidence) (UNUSED)
- Line 434: unused method '_is_SUNW' (60% confidence) (UNUSED)
- Line 436: unused method '_is_sparcstation5' (60% confidence) (UNUSED)
- Line 438: unused method '_is_ultra1' (60% confidence) (UNUSED)
- Line 440: unused method '_is_ultra250' (60% confidence) (UNUSED)
- Line 442: unused method '_is_ultra2' (60% confidence) (UNUSED)
- Line 444: unused method '_is_ultra30' (60% confidence) (UNUSED)
- Line 446: unused method '_is_ultra4' (60% confidence) (UNUSED)
- Line 448: unused method '_is_ultra5_10' (60% confidence) (UNUSED)
- Line 450: unused method '_is_ultra5' (60% confidence) (UNUSED)
- Line 452: unused method '_is_ultra60' (60% confidence) (UNUSED)
- Line 454: unused method '_is_ultra80' (60% confidence) (UNUSED)
- Line 456: unused method '_is_ultraenterprice' (60% confidence) (UNUSED)
- Line 458: unused method '_is_ultraenterprice10k' (60% confidence) (UNUSED)
- Line 460: unused method '_is_sunfire' (60% confidence) (UNUSED)
- Line 462: unused method '_is_ultra' (60% confidence) (UNUSED)
- Line 465: unused method '_is_cpusparcv7' (60% confidence) (UNUSED)
- Line 467: unused method '_is_cpusparcv8' (60% confidence) (UNUSED)
- Line 469: unused method '_is_cpusparcv9' (60% confidence) (UNUSED)
- Line 504: unused variable 'vtpe' (60% confidence) (UNUSED)
- Line 527: unused method '_is_Am486' (60% confidence) (UNUSED)
- Line 530: unused method '_is_Am5x86' (60% confidence) (UNUSED)
- Line 533: unused method '_is_AMDK5' (60% confidence) (UNUSED)
- Line 537: unused method '_is_AMDK6' (60% confidence) (UNUSED)
- Line 541: unused method '_is_AMDK6_2' (60% confidence) (UNUSED)
- Line 545: unused method '_is_AMDK6_3' (60% confidence) (UNUSED)
- Line 549: unused method '_is_AMDK7' (60% confidence) (UNUSED)
- Line 556: unused method '_is_AMD64' (60% confidence) (UNUSED)
- Line 561: unused method '_is_Intel' (60% confidence) (UNUSED)
- Line 564: unused method '_is_i386' (60% confidence) (UNUSED)
- Line 567: unused method '_is_i486' (60% confidence) (UNUSED)
- Line 570: unused method '_is_i586' (60% confidence) (UNUSED)
- Line 573: unused method '_is_i686' (60% confidence) (UNUSED)
- Line 576: unused method '_is_Pentium' (60% confidence) (UNUSED)
- Line 579: unused method '_is_PentiumMMX' (60% confidence) (UNUSED)
- Line 583: unused method '_is_PentiumPro' (60% confidence) (UNUSED)
- Line 587: unused method '_is_PentiumII' (60% confidence) (UNUSED)
- Line 591: unused method '_is_PentiumIII' (60% confidence) (UNUSED)
- Line 595: unused method '_is_PentiumIV' (60% confidence) (UNUSED)
- Line 598: unused method '_is_PentiumM' (60% confidence) (UNUSED)
- Line 602: unused method '_is_Core2' (60% confidence) (UNUSED)
- Line 608: unused method '_is_singleCPU' (60% confidence) (UNUSED)
- Line 611: unused method '_getNCPUs' (60% confidence) (UNUSED)
- Line 614: unused method '_has_mmx' (60% confidence) (UNUSED)
- Line 623: unused method '_has_sse' (60% confidence) (UNUSED)
- Line 635: unused method '_has_sse2' (60% confidence) (UNUSED)
- Line 644: unused method '_has_3dnow' (60% confidence) (UNUSED)
- Line 647: unused method '_has_3dnowext' (60% confidence) (UNUSED)

#### exec_command.py
- Line 99: unused function 'temp_file_name' (60% confidence) (UNUSED)

#### extension.py
- Line 98: unused method 'has_f2py_sources' (60% confidence) (UNUSED)

#### __init__.py
- Line 202: unused variable 'shared_lib_format' (60% confidence) (UNUSED)
- Line 307: unused function 'verify_command_form' (60% confidence) (UNUSED)
- Line 391: unused method 'get_flags_free' (60% confidence) (UNUSED)
- Line 400: unused method 'get_flags_linker_exe' (60% confidence) (UNUSED)
- Line 403: unused method 'get_flags_ar' (60% confidence) (UNUSED)
- Line 416: unused variable 'get_flags_opt_f77' (60% confidence) (UNUSED)
- Line 416: unused variable 'get_flags_opt_f90' (60% confidence) (UNUSED)
- Line 417: unused variable 'get_flags_arch_f90' (60% confidence) (UNUSED)
- Line 418: unused variable 'get_flags_debug_f77' (60% confidence) (UNUSED)
- Line 418: unused variable 'get_flags_debug_f90' (60% confidence) (UNUSED)

#### absoft.py
- Line 16: unused class 'AbsoftFCompiler' (60% confidence) (UNUSED)

#### arm.py
- Line 11: unused class 'ArmFlangCompiler' (60% confidence) (UNUSED)
- Line 50: unused method 'get_flags_free' (60% confidence) (UNUSED)

#### compaq.py
- Line 16: unused class 'CompaqFCompiler' (60% confidence) (UNUSED)
- Line 54: unused class 'CompaqVisualFCompiler' (60% confidence) (UNUSED)

#### environment.py
- Line 28: unused method 'dump_variables' (60% confidence) (UNUSED)

#### fujitsu.py
- Line 11: unused class 'FujitsuFCompiler' (60% confidence) (UNUSED)

#### g95.py
- Line 6: unused class 'G95FCompiler' (60% confidence) (UNUSED)

#### gnu.py
- Line 266: unused class 'Gnu95FCompiler' (60% confidence) (UNUSED)

#### hpux.py
- Line 5: unused class 'HPUXFCompiler' (60% confidence) (UNUSED)

#### ibm.py
- Line 13: unused class 'IBMFCompiler' (60% confidence) (UNUSED)

#### intel.py
- Line 53: unused method 'get_flags_free' (60% confidence) (UNUSED)
- Line 84: unused class 'IntelItaniumFCompiler' (60% confidence) (UNUSED)
- Line 104: unused class 'IntelEM64TFCompiler' (60% confidence) (UNUSED)
- Line 161: unused method 'get_flags_free' (60% confidence) (UNUSED)
- Line 177: unused class 'IntelItaniumVisualFCompiler' (60% confidence) (UNUSED)
- Line 197: unused class 'IntelEM64VisualFCompiler' (60% confidence) (UNUSED)

#### lahey.py
- Line 7: unused class 'LaheyFCompiler' (60% confidence) (UNUSED)

#### mips.py
- Line 6: unused class 'MIPSFCompiler' (60% confidence) (UNUSED)
- Line 46: unused method 'get_flags_arch_f90' (60% confidence) (UNUSED)

#### nag.py
- Line 24: unused class 'NAGFCompiler' (60% confidence) (UNUSED)
- Line 52: unused class 'NAGFORCompiler' (60% confidence) (UNUSED)

#### none.py
- Line 6: unused class 'NoneFCompiler' (60% confidence) (UNUSED)

#### nv.py
- Line 5: unused class 'NVHPCFCompiler' (60% confidence) (UNUSED)

#### pathf95.py
- Line 5: unused class 'PathScaleFCompiler' (60% confidence) (UNUSED)

#### pg.py
- Line 11: unused class 'PGroupFCompiler' (60% confidence) (UNUSED)
- Line 67: unused class 'PGroupFlangCompiler' (60% confidence) (UNUSED)
- Line 105: unused method 'get_flags_free' (60% confidence) (UNUSED)

#### sun.py
- Line 6: unused class 'SunFCompiler' (60% confidence) (UNUSED)
- Line 35: unused method 'get_opt' (60% confidence) (UNUSED)
- Line 37: unused method 'get_arch' (60% confidence) (UNUSED)

#### vast.py
- Line 7: unused class 'VastFCompiler' (60% confidence) (UNUSED)
- Line 33: unused method 'get_version_cmd' (60% confidence) (UNUSED)

#### fujitsuccompiler.py
- Line 3: unused class 'FujitsuCCompiler' (60% confidence) (UNUSED)

#### intelccompiler.py
- Line 38: unused class 'IntelItaniumCCompiler' (60% confidence) (UNUSED)
- Line 43: unused class 'IntelEM64TCCompiler' (60% confidence) (UNUSED)
- Line 96: unused class 'IntelEM64TCCompilerW' (60% confidence) (UNUSED)

#### line_endings.py
- Line 71: unused function 'unix2dos_dir' (60% confidence) (UNUSED)

#### log.py
- Line 24: unsatisfiable 'if' condition (100% confidence) (UNUSED)

#### mingw32ccompiler.py
- Line 40: unused function 'get_msvcr_replacement' (60% confidence) (UNUSED)
- Line 51: unused class 'Mingw32CCompiler' (60% confidence) (UNUSED)
- Line 536: unused function 'manifest_rc' (60% confidence) (UNUSED)

#### misc_util.py
- Line 112: unused function 'quote_args' (60% confidence) (UNUSED)
- Line 1018: unused method 'add_subpackage' (60% confidence) (UNUSED)
- Line 1344: unused method 'add_define_macros' (60% confidence) (UNUSED)
- Line 1360: unused method 'add_include_dirs' (60% confidence) (UNUSED)
- Line 1433: unused method 'add_extension' (60% confidence) (UNUSED)
- Line 1536: unused method 'add_library' (60% confidence) (UNUSED)
- Line 1588: unused method 'add_installed_library' (60% confidence) (UNUSED)
- Line 1639: unused method 'add_npy_pkg_config' (60% confidence) (UNUSED)
- Line 1746: unused method 'add_scripts' (60% confidence) (UNUSED)
- Line 1807: unused attribute 'noisy' (60% confidence) (UNUSED)
- Line 1814: unused method 'get_build_temp_dir' (60% confidence) (UNUSED)
- Line 1823: unused method 'have_f77c' (60% confidence) (UNUSED)
- Line 1842: unused method 'have_f90c' (60% confidence) (UNUSED)
- Line 1861: unused method 'append_to' (60% confidence) (UNUSED)
- Line 2018: unused method 'make_svn_version_py' (60% confidence) (UNUSED)
- Line 2059: unused method 'make_hg_version_py' (60% confidence) (UNUSED)
- Line 2099: unused method 'make_config_py' (60% confidence) (UNUSED)
- Line 2261: unused function 'is_bootstrapping' (60% confidence) (UNUSED)
- Line 2306: unused variable 'pathdrive' (60% confidence) (UNUSED)
- Line 2450: unused function 'msvc_version' (60% confidence) (UNUSED)

#### msvccompiler.py
- Line 61: unused function 'lib_opts_if_msvc' (60% confidence) (UNUSED)

#### npy_pkg_config.py
- Line 232: unused function 'parse_variables' (60% confidence) (UNUSED)
- Line 243: unused function 'parse_sections' (60% confidence) (UNUSED)
- Line 290: unused variable 'nmeta' (60% confidence) (UNUSED)
- Line 290: unused variable 'nreqs' (60% confidence) (UNUSED)

#### numpy_distribution.py
- Line 16: unused method 'has_scons_scripts' (60% confidence) (UNUSED)

#### pathccompiler.py
- Line 3: unused class 'PathScaleCCompiler' (60% confidence) (UNUSED)

#### system_info.py
- Line 727: unused attribute 'local_prefixes' (60% confidence) (UNUSED)
- Line 1858: unused method '_calc_info_armpl' (60% confidence) (UNUSED)
- Line 1865: unused method '_calc_info_mkl' (60% confidence) (UNUSED)
- Line 1872: unused method '_calc_info_ssl2' (60% confidence) (UNUSED)
- Line 1879: unused method '_calc_info_openblas' (60% confidence) (UNUSED)
- Line 1890: unused method '_calc_info_flame' (60% confidence) (UNUSED)
- Line 1897: unused method '_calc_info_atlas' (60% confidence) (UNUSED)
- Line 1922: unused method '_calc_info_accelerate' (60% confidence) (UNUSED)
- Line 1952: unused method '_calc_info_lapack' (60% confidence) (UNUSED)
- Line 2052: unused method '_calc_info_armpl' (60% confidence) (UNUSED)
- Line 2059: unused method '_calc_info_mkl' (60% confidence) (UNUSED)
- Line 2066: unused method '_calc_info_ssl2' (60% confidence) (UNUSED)
- Line 2073: unused method '_calc_info_blis' (60% confidence) (UNUSED)
- Line 2080: unused method '_calc_info_openblas' (60% confidence) (UNUSED)
- Line 2087: unused method '_calc_info_atlas' (60% confidence) (UNUSED)
- Line 2100: unused method '_calc_info_accelerate' (60% confidence) (UNUSED)
- Line 2107: unused method '_calc_info_blas' (60% confidence) (UNUSED)

#### test_exec_command.py
- Line 165: unused method 'check_basic' (60% confidence) (UNUSED)

#### test_system_info.py
- Line 109: unused attribute 'local_prefixes' (60% confidence) (UNUSED)

#### dtypes.py
- Line 30: unused function '_add_dtype_helper' (60% confidence) (UNUSED)

#### _distutils.py
- Line 14: unused variable 'sef' (100% confidence) (UNUSED)

#### _meson.py
- Line 29: unused variable 'linker_args' (100% confidence) (UNUSED)

#### auxfuncs.py
- Line 74: unused function '_isstring' (60% confidence) (UNUSED)
- Line 231: unused function 'isunsignedarray' (60% confidence) (UNUSED)
- Line 241: unused function 'issigned_chararray' (60% confidence) (UNUSED)
- Line 246: unused function 'issigned_shortarray' (60% confidence) (UNUSED)
- Line 251: unused function 'issigned_array' (60% confidence) (UNUSED)
- Line 265: unused function 'ismutable' (60% confidence) (UNUSED)
- Line 402: unused function 'hasvariables' (60% confidence) (UNUSED)
- Line 537: unused function 'hasinitvalueasstring' (60% confidence) (UNUSED)
- Line 592: unused function 'istrue' (60% confidence) (UNUSED)
- Line 596: unused function 'isfalse' (60% confidence) (UNUSED)

#### crackfortran.py
- Line 193: unused variable 'skipfunctions' (60% confidence) (UNUSED)
- Line 228: unused variable 'skipfunctions' (60% confidence) (UNUSED)
- Line 245: unused attribute '_MAXCACHE' (60% confidence) (UNUSED)
- Line 693: unused variable 'crackline_bind_1' (60% confidence) (UNUSED)
- Line 948: unused function '_is_intent_callback' (60% confidence) (UNUSED)
- Line 1955: unused function 'getblockname' (60% confidence) (UNUSED)
- Line 2290: unused function 'getlincoef' (60% confidence) (UNUSED)
- Line 3625: unused variable 'parent_value' (60% confidence) (UNUSED)

#### f90mod_rules.py
- Line 70: unused variable 'fgetdims2_sa' (60% confidence) (UNUSED)

#### symbolic.py
- Line 100: unused variable 'POS' (60% confidence) (UNUSED)
- Line 101: unused variable 'NEG' (60% confidence) (UNUSED)
- Line 124: unused variable 'LAND' (60% confidence) (UNUSED)
- Line 125: unused variable 'LOR' (60% confidence) (UNUSED)
- Line 127: unused variable 'ASSIGN' (60% confidence) (UNUSED)

#### test_array_from_pyobj.py
- Line 39: unused function 'flags_info' (60% confidence) (UNUSED)
- Line 222: unused method 'smaller_types' (60% confidence) (UNUSED)
- Line 230: unused method 'equal_types' (60% confidence) (UNUSED)
- Line 240: unused method 'larger_types' (60% confidence) (UNUSED)
- Line 372: unused method 'setup_type' (60% confidence) (UNUSED)

#### test_callback.py
- Line 175: unused attribute 'global_f' (60% confidence) (UNUSED)
- Line 179: unused attribute 'global_f' (60% confidence) (UNUSED)
- Line 189: unused attribute 'global_f' (60% confidence) (UNUSED)
- Line 260: unused attribute 'mypy_abort' (60% confidence) (UNUSED)

#### test_regression.py
- Line 35: unused variable 'int_in' (60% confidence) (UNUSED)

#### util.py
- Line 378: unused attribute '_has_c_compiler' (60% confidence) (UNUSED)

#### _datasource.py
- Line 45: unused function '_check_mode' (60% confidence) (UNUSED)
- Line 311: unused variable 'ufrag' (60% confidence) (UNUSED)
- Line 311: unused variable 'uparams' (60% confidence) (UNUSED)
- Line 311: unused variable 'uquery' (60% confidence) (UNUSED)
- Line 408: unused variable 'ufrag' (60% confidence) (UNUSED)
- Line 408: unused variable 'uparams' (60% confidence) (UNUSED)
- Line 408: unused variable 'uquery' (60% confidence) (UNUSED)

#### _index_tricks_impl.py
- Line 701: unused method 'ndincr' (60% confidence) (UNUSED)

#### _iotools.py
- Line 48: unused function '_is_bytes_like' (60% confidence) (UNUSED)

#### _polynomial_impl.py
- Line 1229: unused variable 'coefficients' (60% confidence) (UNUSED)

#### _shape_base_impl.py
- Line 729: unused function '_replace_zero_by_x_arrays' (60% confidence) (UNUSED)

#### _stride_tricks_impl.py
- Line 359: unused attribute '_warn_on_write' (60% confidence) (UNUSED)

#### _utils_impl.py
- Line 265: unused function 'deprecate_with_doc' (60% confidence) (UNUSED)

#### format.py
- Line 483: unused function 'write_array_header_2_0' (60% confidence) (UNUSED)

#### test__datasource.py
- Line 77: unused function 'invalid_baseurl' (60% confidence) (UNUSED)
- Line 85: unused function 'invalid_httpfile' (60% confidence) (UNUSED)
- Line 198: unused variable 'frg' (60% confidence) (UNUSED)
- Line 198: unused variable 'pms' (60% confidence) (UNUSED)
- Line 198: unused variable 'qry' (60% confidence) (UNUSED)
- Line 212: unused variable 'frg' (60% confidence) (UNUSED)
- Line 212: unused variable 'pms' (60% confidence) (UNUSED)
- Line 212: unused variable 'qry' (60% confidence) (UNUSED)
- Line 263: unused variable 'frg' (60% confidence) (UNUSED)
- Line 263: unused variable 'pms' (60% confidence) (UNUSED)
- Line 263: unused variable 'qry' (60% confidence) (UNUSED)
- Line 312: unused variable 'frg' (60% confidence) (UNUSED)
- Line 312: unused variable 'pms' (60% confidence) (UNUSED)
- Line 312: unused variable 'qry' (60% confidence) (UNUSED)

#### test_format.py
- Line 959: unused variable 'nps' (60% confidence) (UNUSED)

#### test_histograms.py
- Line 69: unused variable 'dmy' (60% confidence) (UNUSED)
- Line 149: unused variable 'nwb' (60% confidence) (UNUSED)

#### test_recfunctions.py
- Line 12: unused variable 'get_fieldspec' (60% confidence) (UNUSED)
- Line 16: unused variable 'zip_dtype' (60% confidence) (UNUSED)

#### test_stride_tricks.py
- Line 502: unused function 'as_strided_writeable' (60% confidence) (UNUSED)

#### test_twodim_base.py
- Line 243: unused variable 'edge1' (60% confidence) (UNUSED)
- Line 243: unused variable 'edge2' (60% confidence) (UNUSED)
- Line 246: unused variable 'edge1' (60% confidence) (UNUSED)
- Line 246: unused variable 'edge2' (60% confidence) (UNUSED)

#### test_utils.py
- Line 22: unused function 'first_method' (60% confidence) (UNUSED)

#### _linalg.py
- Line 70: unused variable 'fortran_int' (60% confidence) (UNUSED)
- Line 1322: unused function '_convertarray' (60% confidence) (UNUSED)

#### test_linalg.py
- Line 577: unused variable 'evectors' (60% confidence) (UNUSED)
- Line 1119: unused variable 'evectors' (60% confidence) (UNUSED)
- Line 1188: unused variable 'evectors' (60% confidence) (UNUSED)

#### test_regression.py
- Line 47: unused variable 'vecs' (60% confidence) (UNUSED)

#### core.py
- Line 1468: unused variable 'get_mask' (60% confidence) (UNUSED)
- Line 3711: unused method 'unshare_mask' (60% confidence) (UNUSED)
- Line 4603: unused variable 'get_imag' (60% confidence) (UNUSED)
- Line 4631: unused variable 'get_real' (60% confidence) (UNUSED)
- Line 4859: unused variable 'refcheck' (100% confidence) (UNUSED)
- Line 4990: unused method 'iscontiguous' (60% confidence) (UNUSED)
- Line 6527: unused variable 'torecords' (60% confidence) (UNUSED)

#### extras.py
- Line 314: unused class '_fromnxfunction_args' (60% confidence) (UNUSED)

#### mrecords.py
- Line 36: unused function '_checknames' (60% confidence) (UNUSED)
- Line 70: unused method '_get_fieldmask' (60% confidence) (UNUSED)
- Line 163: unused property '_fieldmask' (60% confidence) (UNUSED)

#### test_core.py
- Line 2076: unused attribute '_smallmask' (60% confidence) (UNUSED)

#### test_mrecords.py
- Line 200: unused attribute 'fieldmask' (60% confidence) (UNUSED)

#### testutils.py
- Line 196: unused variable 'assert_close' (60% confidence) (UNUSED)
- Line 245: unused function 'assert_array_approx_equal' (60% confidence) (UNUSED)

#### timer_comparison.py
- Line 12: unused class 'ModuleTester' (60% confidence) (UNUSED)
- Line 45: unused attribute 'testnames' (60% confidence) (UNUSED)
- Line 110: unused method 'test_0' (60% confidence) (UNUSED)
- Line 121: unused method 'test_1' (60% confidence) (UNUSED)
- Line 149: unused method 'test_2' (60% confidence) (UNUSED)
- Line 192: unused method 'test_3' (60% confidence) (UNUSED)
- Line 212: unused method 'test_4' (60% confidence) (UNUSED)
- Line 236: unused method 'test_5' (60% confidence) (UNUSED)
- Line 289: unused method 'test_6' (60% confidence) (UNUSED)
- Line 341: unused method 'test_7' (60% confidence) (UNUSED)
- Line 376: unused method 'test_99' (60% confidence) (UNUSED)
- Line 422: unused method 'test_A' (60% confidence) (UNUSED)

#### defmatrix.py
- Line 1010: unused variable 'getT' (60% confidence) (UNUSED)
- Line 1011: unused variable 'getA' (60% confidence) (UNUSED)
- Line 1012: unused variable 'getA1' (60% confidence) (UNUSED)
- Line 1013: unused variable 'getH' (60% confidence) (UNUSED)
- Line 1014: unused variable 'getI' (60% confidence) (UNUSED)

#### _polybase.py
- Line 188: unused method 'has_samecoef' (60% confidence) (UNUSED)
- Line 209: unused method 'has_samedomain' (60% confidence) (UNUSED)
- Line 225: unused method 'has_samewindow' (60% confidence) (UNUSED)
- Line 241: unused method 'has_sametype' (60% confidence) (UNUSED)

#### chebyshev.py
- Line 277: unused function '_zseries_der' (60% confidence) (UNUSED)
- Line 309: unused function '_zseries_int' (60% confidence) (UNUSED)

#### test_printing.py
- Line 14: unused method 'use_unicode' (60% confidence) (UNUSED)

#### __init__.py
- Line 197: unused function '__RandomState_ctor' (60% confidence) (UNUSED)

#### _pickle.py
- Line 44: unused function '__generator_ctor' (60% confidence) (UNUSED)
- Line 69: unused function '__randomstate_ctor' (60% confidence) (UNUSED)

#### test_direct.py
- Line 200: unused attribute 'seed_error_type' (60% confidence) (UNUSED)
- Line 384: unused attribute 'seed_error_type' (60% confidence) (UNUSED)
- Line 404: unused attribute 'seed_error_type' (60% confidence) (UNUSED)
- Line 444: unused attribute 'seed_error_type' (60% confidence) (UNUSED)
- Line 483: unused attribute 'seed_error_type' (60% confidence) (UNUSED)
- Line 521: unused attribute 'seed_error_type' (60% confidence) (UNUSED)

#### test_generator_mt19937.py
- Line 292: unused attribute 'legacy_state' (60% confidence) (UNUSED)

#### test_randomstate.py
- Line 56: unused function 'restore_singleton_bitgen' (60% confidence) (UNUSED)
- Line 2067: unused variable 'restore_singleton_bitgen' (100% confidence) (UNUSED)
- Line 2078: unused variable 'restore_singleton_bitgen' (100% confidence) (UNUSED)
- Line 2092: unused variable 'restore_singleton_bitgen' (100% confidence) (UNUSED)
- Line 2101: unused variable 'restore_singleton_bitgen' (100% confidence) (UNUSED)
- Line 2119: unused variable 'restore_singleton_bitgen' (100% confidence) (UNUSED)

#### test_smoke.py
- Line 111: unused attribute 'seed_error' (60% confidence) (UNUSED)
- Line 729: unused attribute 'seed_error' (60% confidence) (UNUSED)

#### utils.py
- Line 58: unused variable 'KnownFailureTest' (60% confidence) (UNUSED)

#### overrides.py
- Line 10: unused function 'get_overridable_numpy_ufuncs' (60% confidence) (UNUSED)
- Line 27: unused function 'allows_array_ufunc_override' (60% confidence) (UNUSED)
- Line 69: unused function 'allows_array_function_override' (60% confidence) (UNUSED)

#### test_public_api.py
- Line 305: unused variable 'ispkg' (60% confidence) (UNUSED)

#### array_like.py
- Line 15: unused variable 'x6' (60% confidence) (UNUSED)
- Line 16: unused variable 'x7' (60% confidence) (UNUSED)
- Line 17: unused variable 'x8' (60% confidence) (UNUSED)
- Line 18: unused variable 'x9' (60% confidence) (UNUSED)
- Line 19: unused variable 'x10' (60% confidence) (UNUSED)
- Line 20: unused variable 'x11' (60% confidence) (UNUSED)
- Line 21: unused variable 'x12' (60% confidence) (UNUSED)
- Line 31: unused variable 'x13' (60% confidence) (UNUSED)

#### lib_user_array.py
- Line 20: unused variable 'ua_bool' (60% confidence) (UNUSED)

#### random.py
- Line 493: unused variable 'I_int64_100' (60% confidence) (UNUSED)
- Line 1479: unused variable 'random_st_get_state_legacy' (60% confidence) (UNUSED)

#### shape.py
- Line 8: unused variable 'x_axis' (60% confidence) (UNUSED)
- Line 9: unused variable 'y_axis' (60% confidence) (UNUSED)

#### test_typing.py
- Line 70: unused function 'strip_func' (60% confidence) (UNUSED)
- Line 75: unused function 'run_mypy' (60% confidence) (UNUSED)
- Line 238: unused variable 'path_without_extension' (60% confidence) (UNUSED)

#### __init__.py
- Line 349: unused function '_reset_client' (60% confidence) (UNUSED)

#### _client.py
- Line 251: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 332: unused variable 'with_options' (60% confidence) (UNUSED)
- Line 546: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 627: unused variable 'with_options' (60% confidence) (UNUSED)

#### _compat.py
- Line 103: unused function 'field_outer_type' (60% confidence) (UNUSED)
- Line 209: unused class 'typed_cached_property' (60% confidence) (UNUSED)
- Line 231: unused variable 'typed_cached_property' (60% confidence) (UNUSED)

#### _legacy_response.py
- Line 426: unused method 'write_to_file' (60% confidence) (UNUSED)
- Line 442: unused method 'stream_to_file' (60% confidence) (UNUSED)
- Line 473: unused method 'astream_to_file' (60% confidence) (UNUSED)

#### _models.py
- Line 92: unused property 'model_fields_set' (60% confidence) (UNUSED)
- Line 700: unused function 'set_pydantic_config' (60% confidence) (UNUSED)
- Line 709: unused attribute '_request_id' (60% confidence) (UNUSED)

#### _response.py
- Line 490: unused class 'BinaryAPIResponse' (60% confidence) (UNUSED)
- Line 498: unused method 'write_to_file' (60% confidence) (UNUSED)
- Line 515: unused class 'AsyncBinaryAPIResponse' (60% confidence) (UNUSED)
- Line 523: unused method 'write_to_file' (60% confidence) (UNUSED)
- Line 542: unused method 'stream_to_file' (60% confidence) (UNUSED)
- Line 558: unused method 'stream_to_file' (60% confidence) (UNUSED)
- Line 787: unused function 'to_custom_raw_response_wrapper' (60% confidence) (UNUSED)
- Line 810: unused function 'async_to_custom_raw_response_wrapper' (60% confidence) (UNUSED)

#### _types.py
- Line 31: unused variable 'AsyncTransport' (60% confidence) (UNUSED)
- Line 172: unused variable '__key' (100% confidence) (UNUSED)

#### migrate.py
- Line 64: unused variable 'KEYGEN_ACCOUNT' (60% confidence) (UNUSED)

#### _utils.py
- Line 14: unused variable 'OKBLUE' (60% confidence) (UNUSED)
- Line 15: unused variable 'OKGREEN' (60% confidence) (UNUSED)
- Line 20: unused variable 'UNDERLINE' (60% confidence) (UNUSED)

#### local_audio_player.py
- Line 53: unused method 'play' (60% confidence) (UNUSED)
- Line 104: unused method 'play_stream' (60% confidence) (UNUSED)

#### microphone.py
- Line 35: unused attribute 'has_record_function' (60% confidence) (UNUSED)

#### azure.py
- Line 44: unused class 'MutuallyExclusiveAuthError' (60% confidence) (UNUSED)
- Line 296: unused variable 'with_options' (60% confidence) (UNUSED)
- Line 570: unused variable 'with_options' (60% confidence) (UNUSED)

#### _assistants.py
- Line 29: unused variable 'text_deltas' (60% confidence) (UNUSED)
- Line 54: unused attribute 'text_deltas' (60% confidence) (UNUSED)
- Line 77: unused property 'current_run' (60% confidence) (UNUSED)
- Line 81: unused property 'current_run_step_snapshot' (60% confidence) (UNUSED)
- Line 105: unused method 'get_final_run' (60% confidence) (UNUSED)
- Line 114: unused method 'get_final_run_steps' (60% confidence) (UNUSED)
- Line 123: unused method 'get_final_messages' (60% confidence) (UNUSED)
- Line 153: unused variable 'run_step' (100% confidence) (UNUSED)
- Line 183: unused variable 'run_step' (100% confidence) (UNUSED)
- Line 461: unused variable 'text_deltas' (60% confidence) (UNUSED)
- Line 486: unused attribute 'text_deltas' (60% confidence) (UNUSED)
- Line 518: unused property 'current_run' (60% confidence) (UNUSED)
- Line 522: unused property 'current_run_step_snapshot' (60% confidence) (UNUSED)
- Line 537: unused method 'get_final_run' (60% confidence) (UNUSED)
- Line 546: unused method 'get_final_run_steps' (60% confidence) (UNUSED)
- Line 555: unused method 'get_final_messages' (60% confidence) (UNUSED)
- Line 585: unused variable 'run_step' (100% confidence) (UNUSED)
- Line 615: unused variable 'run_step' (100% confidence) (UNUSED)

#### _events.py
- Line 65: unused variable 'arguments_delta' (60% confidence) (UNUSED)

#### _responses.py
- Line 75: unused method 'get_final_response' (60% confidence) (UNUSED)
- Line 171: unused method 'get_final_response' (60% confidence) (UNUSED)
- Line 233: unused attribute '_rich_text_format' (60% confidence) (UNUSED)

#### audio.py
- Line 58: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 91: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### speech.py
- Line 39: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 130: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 212: unused attribute '_speech' (60% confidence) (UNUSED)
- Line 221: unused attribute '_speech' (60% confidence) (UNUSED)
- Line 230: unused attribute '_speech' (60% confidence) (UNUSED)
- Line 240: unused attribute '_speech' (60% confidence) (UNUSED)

#### transcriptions.py
- Line 45: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 345: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 636: unused attribute '_transcriptions' (60% confidence) (UNUSED)
- Line 645: unused attribute '_transcriptions' (60% confidence) (UNUSED)
- Line 654: unused attribute '_transcriptions' (60% confidence) (UNUSED)
- Line 663: unused attribute '_transcriptions' (60% confidence) (UNUSED)

#### translations.py
- Line 40: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 183: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### batches.py
- Line 36: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 246: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### assistants.py
- Line 45: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 494: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 934: unused attribute '_assistants' (60% confidence) (UNUSED)
- Line 955: unused attribute '_assistants' (60% confidence) (UNUSED)
- Line 976: unused attribute '_assistants' (60% confidence) (UNUSED)
- Line 997: unused attribute '_assistants' (60% confidence) (UNUSED)

#### beta.py
- Line 63: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 100: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### completions.py
- Line 53: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 332: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### realtime.py
- Line 84: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 140: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 234: unused variable 'input_audio_buffer' (60% confidence) (UNUSED)
- Line 235: unused variable 'conversation' (60% confidence) (UNUSED)
- Line 236: unused variable 'output_audio_buffer' (60% confidence) (UNUSED)
- Line 237: unused variable 'transcription_session' (60% confidence) (UNUSED)
- Line 246: unused attribute 'input_audio_buffer' (60% confidence) (UNUSED)
- Line 247: unused attribute 'conversation' (60% confidence) (UNUSED)
- Line 248: unused attribute 'output_audio_buffer' (60% confidence) (UNUSED)
- Line 249: unused attribute 'transcription_session' (60% confidence) (UNUSED)
- Line 416: unused variable 'input_audio_buffer' (60% confidence) (UNUSED)
- Line 417: unused variable 'conversation' (60% confidence) (UNUSED)
- Line 418: unused variable 'output_audio_buffer' (60% confidence) (UNUSED)
- Line 419: unused variable 'transcription_session' (60% confidence) (UNUSED)
- Line 428: unused attribute 'input_audio_buffer' (60% confidence) (UNUSED)
- Line 429: unused attribute 'conversation' (60% confidence) (UNUSED)
- Line 430: unused attribute 'output_audio_buffer' (60% confidence) (UNUSED)
- Line 431: unused attribute 'transcription_session' (60% confidence) (UNUSED)

#### sessions.py
- Line 34: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 200: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 357: unused attribute '_sessions' (60% confidence) (UNUSED)
- Line 366: unused attribute '_sessions' (60% confidence) (UNUSED)
- Line 375: unused attribute '_sessions' (60% confidence) (UNUSED)
- Line 384: unused attribute '_sessions' (60% confidence) (UNUSED)

#### transcription_sessions.py
- Line 34: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 143: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 243: unused attribute '_transcription_sessions' (60% confidence) (UNUSED)
- Line 252: unused attribute '_transcription_sessions' (60% confidence) (UNUSED)
- Line 261: unused attribute '_transcription_sessions' (60% confidence) (UNUSED)
- Line 270: unused attribute '_transcription_sessions' (60% confidence) (UNUSED)

#### messages.py
- Line 41: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 319: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### runs.py
- Line 76: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 861: unused method 'create_and_stream' (60% confidence) (UNUSED)
- Line 893: unused method 'create_and_stream' (60% confidence) (UNUSED)
- Line 926: unused method 'create_and_stream' (60% confidence) (UNUSED)
- Line 1339: unused method 'submit_tool_outputs_and_poll' (60% confidence) (UNUSED)
- Line 1378: unused method 'submit_tool_outputs_stream' (60% confidence) (UNUSED)
- Line 1399: unused method 'submit_tool_outputs_stream' (60% confidence) (UNUSED)
- Line 1421: unused method 'submit_tool_outputs_stream' (60% confidence) (UNUSED)
- Line 1487: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 2272: unused method 'create_and_stream' (60% confidence) (UNUSED)
- Line 2303: unused method 'create_and_stream' (60% confidence) (UNUSED)
- Line 2335: unused method 'create_and_stream' (60% confidence) (UNUSED)
- Line 2749: unused method 'submit_tool_outputs_and_poll' (60% confidence) (UNUSED)
- Line 2788: unused method 'submit_tool_outputs_stream' (60% confidence) (UNUSED)
- Line 2809: unused method 'submit_tool_outputs_stream' (60% confidence) (UNUSED)
- Line 2831: unused method 'submit_tool_outputs_stream' (60% confidence) (UNUSED)

#### steps.py
- Line 36: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 190: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### threads.py
- Line 80: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 729: unused method 'create_and_run_poll' (60% confidence) (UNUSED)
- Line 784: unused method 'create_and_run_stream' (60% confidence) (UNUSED)
- Line 813: unused method 'create_and_run_stream' (60% confidence) (UNUSED)
- Line 843: unused method 'create_and_run_stream' (60% confidence) (UNUSED)
- Line 929: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 1578: unused method 'create_and_run_poll' (60% confidence) (UNUSED)
- Line 1635: unused method 'create_and_run_stream' (60% confidence) (UNUSED)
- Line 1664: unused method 'create_and_run_stream' (60% confidence) (UNUSED)
- Line 1694: unused method 'create_and_run_stream' (60% confidence) (UNUSED)

#### chat.py
- Line 34: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 59: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### completions.py
- Line 66: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 1169: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### messages.py
- Line 34: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 112: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### completions.py
- Line 38: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 588: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### embeddings.py
- Line 38: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 153: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 259: unused attribute '_embeddings' (60% confidence) (UNUSED)
- Line 268: unused attribute '_embeddings' (60% confidence) (UNUSED)
- Line 277: unused attribute '_embeddings' (60% confidence) (UNUSED)
- Line 286: unused attribute '_embeddings' (60% confidence) (UNUSED)

#### evals.py
- Line 52: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 311: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### output_items.py
- Line 35: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 158: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 272: unused attribute '_output_items' (60% confidence) (UNUSED)
- Line 284: unused attribute '_output_items' (60% confidence) (UNUSED)
- Line 296: unused attribute '_output_items' (60% confidence) (UNUSED)
- Line 308: unused attribute '_output_items' (60% confidence) (UNUSED)

#### runs.py
- Line 52: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 301: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### files.py
- Line 46: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 323: unused method 'wait_for_processing' (60% confidence) (UNUSED)
- Line 358: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 635: unused method 'wait_for_processing' (60% confidence) (UNUSED)

#### alpha.py
- Line 34: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 59: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### graders.py
- Line 34: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 136: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 229: unused attribute '_graders' (60% confidence) (UNUSED)
- Line 241: unused attribute '_graders' (60% confidence) (UNUSED)
- Line 253: unused attribute '_graders' (60% confidence) (UNUSED)
- Line 265: unused attribute '_graders' (60% confidence) (UNUSED)

#### checkpoints.py
- Line 34: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 59: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### permissions.py
- Line 37: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 205: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 364: unused attribute '_permissions' (60% confidence) (UNUSED)
- Line 379: unused attribute '_permissions' (60% confidence) (UNUSED)
- Line 394: unused attribute '_permissions' (60% confidence) (UNUSED)
- Line 409: unused attribute '_permissions' (60% confidence) (UNUSED)

#### fine_tuning.py
- Line 58: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 91: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### checkpoints.py
- Line 35: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 106: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### jobs.py
- Line 52: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 430: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### images.py
- Line 35: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 359: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 674: unused attribute '_images' (60% confidence) (UNUSED)
- Line 689: unused attribute '_images' (60% confidence) (UNUSED)
- Line 704: unused attribute '_images' (60% confidence) (UNUSED)
- Line 719: unused attribute '_images' (60% confidence) (UNUSED)

#### models.py
- Line 34: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 147: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### moderations.py
- Line 35: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 105: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 166: unused attribute '_moderations' (60% confidence) (UNUSED)
- Line 175: unused attribute '_moderations' (60% confidence) (UNUSED)
- Line 184: unused attribute '_moderations' (60% confidence) (UNUSED)
- Line 193: unused attribute '_moderations' (60% confidence) (UNUSED)

#### input_items.py
- Line 36: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 124: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 203: unused attribute '_input_items' (60% confidence) (UNUSED)
- Line 212: unused attribute '_input_items' (60% confidence) (UNUSED)
- Line 221: unused attribute '_input_items' (60% confidence) (UNUSED)
- Line 230: unused attribute '_input_items' (60% confidence) (UNUSED)

#### responses.py
- Line 65: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 953: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### parts.py
- Line 33: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 108: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### uploads.py
- Line 58: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 67: unused method 'upload_file_chunked' (60% confidence) (UNUSED)
- Line 80: unused method 'upload_file_chunked' (60% confidence) (UNUSED)
- Line 94: unused method 'upload_file_chunked' (60% confidence) (UNUSED)
- Line 350: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 359: unused method 'upload_file_chunked' (60% confidence) (UNUSED)
- Line 372: unused method 'upload_file_chunked' (60% confidence) (UNUSED)
- Line 386: unused method 'upload_file_chunked' (60% confidence) (UNUSED)

#### file_batches.py
- Line 42: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 317: unused method 'upload_and_poll' (60% confidence) (UNUSED)
- Line 379: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 654: unused method 'upload_and_poll' (60% confidence) (UNUSED)
- Line 730: unused attribute '_file_batches' (60% confidence) (UNUSED)
- Line 748: unused attribute '_file_batches' (60% confidence) (UNUSED)
- Line 766: unused attribute '_file_batches' (60% confidence) (UNUSED)
- Line 784: unused attribute '_file_batches' (60% confidence) (UNUSED)

#### files.py
- Line 39: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 375: unused method 'upload_and_poll' (60% confidence) (UNUSED)
- Line 442: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 780: unused method 'upload_and_poll' (60% confidence) (UNUSED)

#### vector_stores.py
- Line 69: unused method 'with_streaming_response' (60% confidence) (UNUSED)
- Line 414: unused method 'with_streaming_response' (60% confidence) (UNUSED)

#### transcription.py
- Line 17: unused variable 'logprob' (60% confidence) (UNUSED)

#### transcription_segment.py
- Line 14: unused variable 'avg_logprob' (60% confidence) (UNUSED)
- Line 20: unused variable 'compression_ratio' (60% confidence) (UNUSED)
- Line 29: unused variable 'no_speech_prob' (60% confidence) (UNUSED)

#### transcription_text_delta_event.py
- Line 18: unused variable 'logprob' (60% confidence) (UNUSED)

#### transcription_text_done_event.py
- Line 18: unused variable 'logprob' (60% confidence) (UNUSED)

#### batch.py
- Line 27: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 44: unused variable 'cancelled_at' (60% confidence) (UNUSED)
- Line 47: unused variable 'cancelling_at' (60% confidence) (UNUSED)
- Line 50: unused variable 'completed_at' (60% confidence) (UNUSED)
- Line 53: unused variable 'error_file_id' (60% confidence) (UNUSED)
- Line 58: unused variable 'expired_at' (60% confidence) (UNUSED)
- Line 61: unused variable 'expires_at' (60% confidence) (UNUSED)
- Line 64: unused variable 'failed_at' (60% confidence) (UNUSED)
- Line 67: unused variable 'finalizing_at' (60% confidence) (UNUSED)
- Line 70: unused variable 'in_progress_at' (60% confidence) (UNUSED)
- Line 83: unused variable 'output_file_id' (60% confidence) (UNUSED)
- Line 86: unused variable 'request_counts' (60% confidence) (UNUSED)

#### assistant.py
- Line 24: unused variable 'vector_store_ids' (60% confidence) (UNUSED)
- Line 34: unused variable 'code_interpreter' (60% confidence) (UNUSED)
- Line 36: unused variable 'file_search' (60% confidence) (UNUSED)
- Line 43: unused variable 'created_at' (60% confidence) (UNUSED)

#### assistant_create_params.py
- Line 140: unused variable 'chunk_overlap_tokens' (60% confidence) (UNUSED)
- Line 146: unused variable 'max_chunk_size_tokens' (60% confidence) (UNUSED)
- Line 192: unused variable 'vector_store_ids' (60% confidence) (UNUSED)
- Line 210: unused variable 'code_interpreter' (60% confidence) (UNUSED)
- Line 212: unused variable 'file_search' (60% confidence) (UNUSED)

#### assistant_update_params.py
- Line 165: unused variable 'vector_store_ids' (60% confidence) (UNUSED)
- Line 175: unused variable 'code_interpreter' (60% confidence) (UNUSED)
- Line 177: unused variable 'file_search' (60% confidence) (UNUSED)

#### file_search_tool.py
- Line 12: unused variable 'score_threshold' (60% confidence) (UNUSED)
- Line 54: unused variable 'file_search' (60% confidence) (UNUSED)

#### file_search_tool_param.py
- Line 11: unused variable 'score_threshold' (60% confidence) (UNUSED)
- Line 53: unused variable 'file_search' (60% confidence) (UNUSED)

#### conversation_created_event.py
- Line 20: unused variable 'conversation' (60% confidence) (UNUSED)

#### conversation_item.py
- Line 23: unused variable 'call_id' (60% confidence) (UNUSED)

#### conversation_item_content.py
- Line 25: unused variable 'transcript' (60% confidence) (UNUSED)

#### conversation_item_content_param.py
- Line 24: unused variable 'transcript' (60% confidence) (UNUSED)

#### conversation_item_input_audio_transcription_completed_event.py
- Line 18: unused variable 'logprob' (60% confidence) (UNUSED)
- Line 32: unused variable 'transcript' (60% confidence) (UNUSED)

#### conversation_item_input_audio_transcription_delta_event.py
- Line 18: unused variable 'logprob' (60% confidence) (UNUSED)

#### conversation_item_param.py
- Line 24: unused variable 'call_id' (60% confidence) (UNUSED)

#### conversation_item_with_reference.py
- Line 26: unused variable 'call_id' (60% confidence) (UNUSED)

#### conversation_item_with_reference_param.py
- Line 27: unused variable 'call_id' (60% confidence) (UNUSED)

#### input_audio_buffer_speech_started_event.py
- Line 11: unused variable 'audio_start_ms' (60% confidence) (UNUSED)

#### rate_limits_updated_event.py
- Line 21: unused variable 'reset_seconds' (60% confidence) (UNUSED)
- Line 29: unused variable 'rate_limits' (60% confidence) (UNUSED)

#### realtime_response.py
- Line 19: unused variable 'conversation_id' (60% confidence) (UNUSED)
- Line 69: unused variable 'status_details' (60% confidence) (UNUSED)

#### realtime_response_usage.py
- Line 11: unused variable 'audio_tokens' (60% confidence) (UNUSED)
- Line 14: unused variable 'cached_tokens' (60% confidence) (UNUSED)
- Line 17: unused variable 'text_tokens' (60% confidence) (UNUSED)
- Line 22: unused variable 'audio_tokens' (60% confidence) (UNUSED)
- Line 25: unused variable 'text_tokens' (60% confidence) (UNUSED)
- Line 30: unused variable 'input_token_details' (60% confidence) (UNUSED)
- Line 33: unused variable 'input_tokens' (60% confidence) (UNUSED)
- Line 39: unused variable 'output_token_details' (60% confidence) (UNUSED)
- Line 42: unused variable 'output_tokens' (60% confidence) (UNUSED)

#### response_audio_transcript_done_event.py
- Line 26: unused variable 'transcript' (60% confidence) (UNUSED)

#### response_content_part_added_event.py
- Line 18: unused variable 'transcript' (60% confidence) (UNUSED)

#### response_content_part_done_event.py
- Line 18: unused variable 'transcript' (60% confidence) (UNUSED)

#### response_create_event.py
- Line 31: unused variable 'conversation' (60% confidence) (UNUSED)

#### response_create_event_param.py
- Line 32: unused variable 'conversation' (60% confidence) (UNUSED)

#### response_function_call_arguments_delta_event.py
- Line 11: unused variable 'call_id' (60% confidence) (UNUSED)

#### response_function_call_arguments_done_event.py
- Line 14: unused variable 'call_id' (60% confidence) (UNUSED)

#### session.py
- Line 63: unused variable 'create_response' (60% confidence) (UNUSED)
- Line 69: unused variable 'eagerness' (60% confidence) (UNUSED)
- Line 77: unused variable 'interrupt_response' (60% confidence) (UNUSED)
- Line 84: unused variable 'prefix_padding_ms' (60% confidence) (UNUSED)
- Line 91: unused variable 'silence_duration_ms' (60% confidence) (UNUSED)

#### session_create_params.py
- Line 179: unused variable 'create_response' (60% confidence) (UNUSED)
- Line 185: unused variable 'eagerness' (60% confidence) (UNUSED)
- Line 193: unused variable 'interrupt_response' (60% confidence) (UNUSED)
- Line 200: unused variable 'prefix_padding_ms' (60% confidence) (UNUSED)
- Line 207: unused variable 'silence_duration_ms' (60% confidence) (UNUSED)

#### session_create_response.py
- Line 12: unused variable 'expires_at' (60% confidence) (UNUSED)
- Line 52: unused variable 'prefix_padding_ms' (60% confidence) (UNUSED)
- Line 58: unused variable 'silence_duration_ms' (60% confidence) (UNUSED)

#### session_update_event.py
- Line 70: unused variable 'create_response' (60% confidence) (UNUSED)
- Line 76: unused variable 'eagerness' (60% confidence) (UNUSED)
- Line 84: unused variable 'interrupt_response' (60% confidence) (UNUSED)
- Line 91: unused variable 'prefix_padding_ms' (60% confidence) (UNUSED)
- Line 98: unused variable 'silence_duration_ms' (60% confidence) (UNUSED)

#### session_update_event_param.py
- Line 70: unused variable 'create_response' (60% confidence) (UNUSED)
- Line 76: unused variable 'eagerness' (60% confidence) (UNUSED)
- Line 84: unused variable 'interrupt_response' (60% confidence) (UNUSED)
- Line 91: unused variable 'prefix_padding_ms' (60% confidence) (UNUSED)
- Line 98: unused variable 'silence_duration_ms' (60% confidence) (UNUSED)

#### transcription_session.py
- Line 12: unused variable 'expires_at' (60% confidence) (UNUSED)
- Line 51: unused variable 'prefix_padding_ms' (60% confidence) (UNUSED)
- Line 57: unused variable 'silence_duration_ms' (60% confidence) (UNUSED)

#### transcription_session_create_params.py
- Line 98: unused variable 'create_response' (60% confidence) (UNUSED)
- Line 105: unused variable 'eagerness' (60% confidence) (UNUSED)
- Line 113: unused variable 'interrupt_response' (60% confidence) (UNUSED)
- Line 120: unused variable 'prefix_padding_ms' (60% confidence) (UNUSED)
- Line 127: unused variable 'silence_duration_ms' (60% confidence) (UNUSED)

#### transcription_session_update.py
- Line 52: unused variable 'create_response' (60% confidence) (UNUSED)
- Line 59: unused variable 'eagerness' (60% confidence) (UNUSED)
- Line 67: unused variable 'interrupt_response' (60% confidence) (UNUSED)
- Line 74: unused variable 'prefix_padding_ms' (60% confidence) (UNUSED)
- Line 81: unused variable 'silence_duration_ms' (60% confidence) (UNUSED)

#### transcription_session_update_param.py
- Line 52: unused variable 'create_response' (60% confidence) (UNUSED)
- Line 59: unused variable 'eagerness' (60% confidence) (UNUSED)
- Line 67: unused variable 'interrupt_response' (60% confidence) (UNUSED)
- Line 74: unused variable 'prefix_padding_ms' (60% confidence) (UNUSED)
- Line 81: unused variable 'silence_duration_ms' (60% confidence) (UNUSED)

#### thread.py
- Line 22: unused variable 'vector_store_ids' (60% confidence) (UNUSED)
- Line 32: unused variable 'code_interpreter' (60% confidence) (UNUSED)
- Line 34: unused variable 'file_search' (60% confidence) (UNUSED)
- Line 41: unused variable 'created_at' (60% confidence) (UNUSED)

#### thread_create_and_run_params.py
- Line 234: unused variable 'chunk_overlap_tokens' (60% confidence) (UNUSED)
- Line 240: unused variable 'max_chunk_size_tokens' (60% confidence) (UNUSED)
- Line 287: unused variable 'vector_store_ids' (60% confidence) (UNUSED)
- Line 305: unused variable 'code_interpreter' (60% confidence) (UNUSED)
- Line 307: unused variable 'file_search' (60% confidence) (UNUSED)
- Line 346: unused variable 'vector_store_ids' (60% confidence) (UNUSED)
- Line 356: unused variable 'code_interpreter' (60% confidence) (UNUSED)
- Line 358: unused variable 'file_search' (60% confidence) (UNUSED)
- Line 371: unused variable 'last_messages' (60% confidence) (UNUSED)

#### thread_create_params.py
- Line 113: unused variable 'chunk_overlap_tokens' (60% confidence) (UNUSED)
- Line 119: unused variable 'max_chunk_size_tokens' (60% confidence) (UNUSED)
- Line 165: unused variable 'vector_store_ids' (60% confidence) (UNUSED)
- Line 183: unused variable 'code_interpreter' (60% confidence) (UNUSED)
- Line 185: unused variable 'file_search' (60% confidence) (UNUSED)

#### thread_update_params.py
- Line 43: unused variable 'vector_store_ids' (60% confidence) (UNUSED)
- Line 53: unused variable 'code_interpreter' (60% confidence) (UNUSED)
- Line 55: unused variable 'file_search' (60% confidence) (UNUSED)

#### file_citation_annotation.py
- Line 18: unused variable 'file_citation' (60% confidence) (UNUSED)

#### file_citation_delta_annotation.py
- Line 28: unused variable 'file_citation' (60% confidence) (UNUSED)

#### message.py
- Line 55: unused variable 'completed_at' (60% confidence) (UNUSED)
- Line 61: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 64: unused variable 'incomplete_at' (60% confidence) (UNUSED)
- Line 67: unused variable 'incomplete_details' (60% confidence) (UNUSED)

#### run.py
- Line 65: unused variable 'last_messages' (60% confidence) (UNUSED)
- Line 73: unused variable 'completion_tokens' (60% confidence) (UNUSED)
- Line 76: unused variable 'prompt_tokens' (60% confidence) (UNUSED)
- Line 94: unused variable 'cancelled_at' (60% confidence) (UNUSED)
- Line 97: unused variable 'completed_at' (60% confidence) (UNUSED)
- Line 100: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 103: unused variable 'expires_at' (60% confidence) (UNUSED)
- Line 106: unused variable 'failed_at' (60% confidence) (UNUSED)
- Line 109: unused variable 'incomplete_details' (60% confidence) (UNUSED)
- Line 164: unused variable 'required_action' (60% confidence) (UNUSED)
- Line 194: unused variable 'started_at' (60% confidence) (UNUSED)

#### run_create_params.py
- Line 236: unused variable 'last_messages' (60% confidence) (UNUSED)

#### run_submit_tool_outputs_params.py
- Line 27: unused variable 'tool_call_id' (60% confidence) (UNUSED)

#### code_interpreter_tool_call.py
- Line 63: unused variable 'code_interpreter' (60% confidence) (UNUSED)

#### code_interpreter_tool_call_delta.py
- Line 43: unused variable 'code_interpreter' (60% confidence) (UNUSED)

#### file_search_tool_call.py
- Line 24: unused variable 'score_threshold' (60% confidence) (UNUSED)
- Line 71: unused variable 'file_search' (60% confidence) (UNUSED)

#### file_search_tool_call_delta.py
- Line 12: unused variable 'file_search' (60% confidence) (UNUSED)

#### message_creation_step_details.py
- Line 16: unused variable 'message_creation' (60% confidence) (UNUSED)

#### run_step.py
- Line 29: unused variable 'completion_tokens' (60% confidence) (UNUSED)
- Line 32: unused variable 'prompt_tokens' (60% confidence) (UNUSED)
- Line 50: unused variable 'cancelled_at' (60% confidence) (UNUSED)
- Line 53: unused variable 'completed_at' (60% confidence) (UNUSED)
- Line 56: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 59: unused variable 'expired_at' (60% confidence) (UNUSED)
- Line 65: unused variable 'failed_at' (60% confidence) (UNUSED)

#### run_step_delta_message_delta.py
- Line 20: unused variable 'message_creation' (60% confidence) (UNUSED)

#### chat_completion_audio.py
- Line 18: unused variable 'expires_at' (60% confidence) (UNUSED)
- Line 24: unused variable 'transcript' (60% confidence) (UNUSED)

#### chat_completion_content_part_input_audio_param.py
- Line 19: unused variable 'input_audio' (60% confidence) (UNUSED)

#### chat_completion_message.py
- Line 31: unused variable 'url_citation' (60% confidence) (UNUSED)

#### chat_completion_stream_options_param.py
- Line 11: unused variable 'include_usage' (60% confidence) (UNUSED)

#### chat_completion_token_logprob.py
- Line 22: unused variable 'logprob' (60% confidence) (UNUSED)
- Line 43: unused variable 'logprob' (60% confidence) (UNUSED)

#### chat_completion_tool_message_param.py
- Line 20: unused variable 'tool_call_id' (60% confidence) (UNUSED)

#### completion_create_params.py
- Line 342: unused variable 'city' (60% confidence) (UNUSED)
- Line 345: unused variable 'country' (60% confidence) (UNUSED)
- Line 362: unused variable 'approximate' (60% confidence) (UNUSED)
- Line 370: unused variable 'search_context_size' (60% confidence) (UNUSED)
- Line 376: unused variable 'user_location' (60% confidence) (UNUSED)

#### completion_choice.py
- Line 12: unused variable 'text_offset' (60% confidence) (UNUSED)
- Line 14: unused variable 'token_logprobs' (60% confidence) (UNUSED)

#### completion_usage.py
- Line 11: unused variable 'accepted_prediction_tokens' (60% confidence) (UNUSED)
- Line 17: unused variable 'audio_tokens' (60% confidence) (UNUSED)
- Line 20: unused variable 'reasoning_tokens' (60% confidence) (UNUSED)
- Line 23: unused variable 'rejected_prediction_tokens' (60% confidence) (UNUSED)
- Line 33: unused variable 'audio_tokens' (60% confidence) (UNUSED)
- Line 36: unused variable 'cached_tokens' (60% confidence) (UNUSED)
- Line 41: unused variable 'completion_tokens' (60% confidence) (UNUSED)
- Line 44: unused variable 'prompt_tokens' (60% confidence) (UNUSED)
- Line 50: unused variable 'completion_tokens_details' (60% confidence) (UNUSED)
- Line 53: unused variable 'prompt_tokens_details' (60% confidence) (UNUSED)

#### create_embedding_response.py
- Line 13: unused variable 'prompt_tokens' (60% confidence) (UNUSED)

#### eval_create_params.py
- Line 61: unused variable 'include_sample_schema' (60% confidence) (UNUSED)
- Line 135: unused variable 'passing_labels' (60% confidence) (UNUSED)
- Line 143: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 148: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 153: unused variable 'pass_threshold' (60% confidence) (UNUSED)

#### eval_create_response.py
- Line 33: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 39: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 45: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 62: unused variable 'created_at' (60% confidence) (UNUSED)

#### eval_list_response.py
- Line 33: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 39: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 45: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 62: unused variable 'created_at' (60% confidence) (UNUSED)

#### eval_retrieve_response.py
- Line 33: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 39: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 45: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 62: unused variable 'created_at' (60% confidence) (UNUSED)

#### eval_update_response.py
- Line 33: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 39: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 45: unused variable 'pass_threshold' (60% confidence) (UNUSED)
- Line 62: unused variable 'created_at' (60% confidence) (UNUSED)

#### create_eval_completions_run_data_source.py
- Line 56: unused variable 'created_after' (60% confidence) (UNUSED)
- Line 59: unused variable 'created_before' (60% confidence) (UNUSED)
- Line 128: unused variable 'item_reference' (60% confidence) (UNUSED)
- Line 161: unused variable 'input_messages' (60% confidence) (UNUSED)
- Line 166: unused variable 'sampling_params' (60% confidence) (UNUSED)

#### create_eval_completions_run_data_source_param.py
- Line 56: unused variable 'created_after' (60% confidence) (UNUSED)
- Line 59: unused variable 'created_before' (60% confidence) (UNUSED)
- Line 124: unused variable 'item_reference' (60% confidence) (UNUSED)
- Line 155: unused variable 'input_messages' (60% confidence) (UNUSED)
- Line 160: unused variable 'sampling_params' (60% confidence) (UNUSED)

#### run_cancel_response.py
- Line 67: unused variable 'allow_parallel_tool_calls' (60% confidence) (UNUSED)
- Line 73: unused variable 'created_after' (60% confidence) (UNUSED)
- Line 79: unused variable 'created_before' (60% confidence) (UNUSED)
- Line 85: unused variable 'has_tool_calls' (60% confidence) (UNUSED)
- Line 91: unused variable 'instructions_search' (60% confidence) (UNUSED)
- Line 186: unused variable 'item_reference' (60% confidence) (UNUSED)
- Line 220: unused variable 'input_messages' (60% confidence) (UNUSED)
- Line 225: unused variable 'sampling_params' (60% confidence) (UNUSED)
- Line 235: unused variable 'cached_tokens' (60% confidence) (UNUSED)
- Line 238: unused variable 'completion_tokens' (60% confidence) (UNUSED)
- Line 241: unused variable 'invocation_count' (60% confidence) (UNUSED)
- Line 244: unused variable 'run_model_name' (60% confidence) (UNUSED)
- Line 247: unused variable 'prompt_tokens' (60% confidence) (UNUSED)
- Line 266: unused variable 'errored' (60% confidence) (UNUSED)
- Line 283: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 314: unused variable 'per_model_usage' (60% confidence) (UNUSED)
- Line 317: unused variable 'per_testing_criteria_results' (60% confidence) (UNUSED)
- Line 320: unused variable 'report_url' (60% confidence) (UNUSED)
- Line 323: unused variable 'result_counts' (60% confidence) (UNUSED)

#### run_create_params.py
- Line 79: unused variable 'allow_parallel_tool_calls' (60% confidence) (UNUSED)
- Line 85: unused variable 'created_after' (60% confidence) (UNUSED)
- Line 91: unused variable 'created_before' (60% confidence) (UNUSED)
- Line 97: unused variable 'has_tool_calls' (60% confidence) (UNUSED)
- Line 103: unused variable 'instructions_search' (60% confidence) (UNUSED)
- Line 201: unused variable 'item_reference' (60% confidence) (UNUSED)
- Line 235: unused variable 'input_messages' (60% confidence) (UNUSED)
- Line 240: unused variable 'sampling_params' (60% confidence) (UNUSED)

#### run_create_response.py
- Line 67: unused variable 'allow_parallel_tool_calls' (60% confidence) (UNUSED)
- Line 73: unused variable 'created_after' (60% confidence) (UNUSED)
- Line 79: unused variable 'created_before' (60% confidence) (UNUSED)
- Line 85: unused variable 'has_tool_calls' (60% confidence) (UNUSED)
- Line 91: unused variable 'instructions_search' (60% confidence) (UNUSED)
- Line 186: unused variable 'item_reference' (60% confidence) (UNUSED)
- Line 220: unused variable 'input_messages' (60% confidence) (UNUSED)
- Line 225: unused variable 'sampling_params' (60% confidence) (UNUSED)
- Line 235: unused variable 'cached_tokens' (60% confidence) (UNUSED)
- Line 238: unused variable 'completion_tokens' (60% confidence) (UNUSED)
- Line 241: unused variable 'invocation_count' (60% confidence) (UNUSED)
- Line 244: unused variable 'run_model_name' (60% confidence) (UNUSED)
- Line 247: unused variable 'prompt_tokens' (60% confidence) (UNUSED)
- Line 266: unused variable 'errored' (60% confidence) (UNUSED)
- Line 283: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 314: unused variable 'per_model_usage' (60% confidence) (UNUSED)
- Line 317: unused variable 'per_testing_criteria_results' (60% confidence) (UNUSED)
- Line 320: unused variable 'report_url' (60% confidence) (UNUSED)
- Line 323: unused variable 'result_counts' (60% confidence) (UNUSED)

#### run_list_response.py
- Line 67: unused variable 'allow_parallel_tool_calls' (60% confidence) (UNUSED)
- Line 73: unused variable 'created_after' (60% confidence) (UNUSED)
- Line 79: unused variable 'created_before' (60% confidence) (UNUSED)
- Line 85: unused variable 'has_tool_calls' (60% confidence) (UNUSED)
- Line 91: unused variable 'instructions_search' (60% confidence) (UNUSED)
- Line 186: unused variable 'item_reference' (60% confidence) (UNUSED)
- Line 220: unused variable 'input_messages' (60% confidence) (UNUSED)
- Line 225: unused variable 'sampling_params' (60% confidence) (UNUSED)
- Line 235: unused variable 'cached_tokens' (60% confidence) (UNUSED)
- Line 238: unused variable 'completion_tokens' (60% confidence) (UNUSED)
- Line 241: unused variable 'invocation_count' (60% confidence) (UNUSED)
- Line 244: unused variable 'run_model_name' (60% confidence) (UNUSED)
- Line 247: unused variable 'prompt_tokens' (60% confidence) (UNUSED)
- Line 266: unused variable 'errored' (60% confidence) (UNUSED)
- Line 283: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 314: unused variable 'per_model_usage' (60% confidence) (UNUSED)
- Line 317: unused variable 'per_testing_criteria_results' (60% confidence) (UNUSED)
- Line 320: unused variable 'report_url' (60% confidence) (UNUSED)
- Line 323: unused variable 'result_counts' (60% confidence) (UNUSED)

#### run_retrieve_response.py
- Line 67: unused variable 'allow_parallel_tool_calls' (60% confidence) (UNUSED)
- Line 73: unused variable 'created_after' (60% confidence) (UNUSED)
- Line 79: unused variable 'created_before' (60% confidence) (UNUSED)
- Line 85: unused variable 'has_tool_calls' (60% confidence) (UNUSED)
- Line 91: unused variable 'instructions_search' (60% confidence) (UNUSED)
- Line 186: unused variable 'item_reference' (60% confidence) (UNUSED)
- Line 220: unused variable 'input_messages' (60% confidence) (UNUSED)
- Line 225: unused variable 'sampling_params' (60% confidence) (UNUSED)
- Line 235: unused variable 'cached_tokens' (60% confidence) (UNUSED)
- Line 238: unused variable 'completion_tokens' (60% confidence) (UNUSED)
- Line 241: unused variable 'invocation_count' (60% confidence) (UNUSED)
- Line 244: unused variable 'run_model_name' (60% confidence) (UNUSED)
- Line 247: unused variable 'prompt_tokens' (60% confidence) (UNUSED)
- Line 266: unused variable 'errored' (60% confidence) (UNUSED)
- Line 283: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 314: unused variable 'per_model_usage' (60% confidence) (UNUSED)
- Line 317: unused variable 'per_testing_criteria_results' (60% confidence) (UNUSED)
- Line 320: unused variable 'report_url' (60% confidence) (UNUSED)
- Line 323: unused variable 'result_counts' (60% confidence) (UNUSED)

#### output_item_list_response.py
- Line 30: unused variable 'cached_tokens' (60% confidence) (UNUSED)
- Line 33: unused variable 'completion_tokens' (60% confidence) (UNUSED)
- Line 36: unused variable 'prompt_tokens' (60% confidence) (UNUSED)
- Line 79: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 82: unused variable 'datasource_item' (60% confidence) (UNUSED)
- Line 85: unused variable 'datasource_item_id' (60% confidence) (UNUSED)

#### output_item_retrieve_response.py
- Line 30: unused variable 'cached_tokens' (60% confidence) (UNUSED)
- Line 33: unused variable 'completion_tokens' (60% confidence) (UNUSED)
- Line 36: unused variable 'prompt_tokens' (60% confidence) (UNUSED)
- Line 79: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 82: unused variable 'datasource_item' (60% confidence) (UNUSED)
- Line 85: unused variable 'datasource_item_id' (60% confidence) (UNUSED)

#### file_object.py
- Line 18: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 43: unused variable 'expires_at' (60% confidence) (UNUSED)
- Line 46: unused variable 'status_details' (60% confidence) (UNUSED)

#### grader_run_response.py
- Line 13: unused variable 'formula_parse_error' (60% confidence) (UNUSED)
- Line 15: unused variable 'invalid_variable_error' (60% confidence) (UNUSED)
- Line 17: unused variable 'api_model_grader_parse_error' (60% confidence) (UNUSED)
- Line 19: unused variable 'api_model_grader_refusal_error' (60% confidence) (UNUSED)
- Line 21: unused variable 'api_model_grader_server_error' (60% confidence) (UNUSED)
- Line 23: unused variable 'api_model_grader_server_error_details' (60% confidence) (UNUSED)
- Line 27: unused variable 'other_error' (60% confidence) (UNUSED)
- Line 29: unused variable 'python_grader_runtime_error' (60% confidence) (UNUSED)
- Line 31: unused variable 'python_grader_runtime_error_details' (60% confidence) (UNUSED)
- Line 33: unused variable 'python_grader_server_error' (60% confidence) (UNUSED)
- Line 35: unused variable 'python_grader_server_error_type' (60% confidence) (UNUSED)
- Line 37: unused variable 'sample_parse_error' (60% confidence) (UNUSED)
- Line 39: unused variable 'truncated_observation_error' (60% confidence) (UNUSED)
- Line 41: unused variable 'unresponsive_reward_error' (60% confidence) (UNUSED)
- Line 51: unused variable 'sampled_model_name' (60% confidence) (UNUSED)
- Line 55: unused variable 'token_usage' (60% confidence) (UNUSED)
- Line 63: unused variable 'api_model_grader_token_usage_per_model' (60% confidence) (UNUSED)
- Line 65: unused variable 'reward' (60% confidence) (UNUSED)
- Line 67: unused variable 'sub_rewards' (60% confidence) (UNUSED)

#### permission_create_response.py
- Line 14: unused variable 'created_at' (60% confidence) (UNUSED)

#### permission_retrieve_response.py
- Line 15: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 32: unused variable 'first_id' (60% confidence) (UNUSED)
- Line 34: unused variable 'last_id' (60% confidence) (UNUSED)

#### dpo_hyperparameters.py
- Line 26: unused variable 'learning_rate_multiplier' (60% confidence) (UNUSED)
- Line 32: unused variable 'n_epochs' (60% confidence) (UNUSED)

#### dpo_hyperparameters_param.py
- Line 26: unused variable 'learning_rate_multiplier' (60% confidence) (UNUSED)
- Line 32: unused variable 'n_epochs' (60% confidence) (UNUSED)

#### fine_tuning_job.py
- Line 38: unused variable 'learning_rate_multiplier' (60% confidence) (UNUSED)
- Line 44: unused variable 'n_epochs' (60% confidence) (UNUSED)
- Line 55: unused variable 'dpo' (60% confidence) (UNUSED)
- Line 58: unused variable 'reinforcement' (60% confidence) (UNUSED)
- Line 61: unused variable 'supervised' (60% confidence) (UNUSED)
- Line 69: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 78: unused variable 'fine_tuned_model' (60% confidence) (UNUSED)
- Line 84: unused variable 'finished_at' (60% confidence) (UNUSED)
- Line 102: unused variable 'organization_id' (60% confidence) (UNUSED)
- Line 105: unused variable 'result_files' (60% confidence) (UNUSED)
- Line 121: unused variable 'trained_tokens' (60% confidence) (UNUSED)
- Line 141: unused variable 'estimated_finish' (60% confidence) (UNUSED)

#### fine_tuning_job_event.py
- Line 16: unused variable 'created_at' (60% confidence) (UNUSED)

#### fine_tuning_job_wandb_integration_object.py
- Line 15: unused variable 'wandb' (60% confidence) (UNUSED)

#### job_create_params.py
- Line 107: unused variable 'learning_rate_multiplier' (60% confidence) (UNUSED)
- Line 113: unused variable 'n_epochs' (60% confidence) (UNUSED)
- Line 153: unused variable 'wandb' (60% confidence) (UNUSED)
- Line 166: unused variable 'dpo' (60% confidence) (UNUSED)
- Line 169: unused variable 'reinforcement' (60% confidence) (UNUSED)
- Line 172: unused variable 'supervised' (60% confidence) (UNUSED)

#### fine_tuning_job_checkpoint.py
- Line 12: unused variable 'full_valid_loss' (60% confidence) (UNUSED)
- Line 14: unused variable 'full_valid_mean_token_accuracy' (60% confidence) (UNUSED)
- Line 18: unused variable 'train_loss' (60% confidence) (UNUSED)
- Line 20: unused variable 'train_mean_token_accuracy' (60% confidence) (UNUSED)
- Line 22: unused variable 'valid_loss' (60% confidence) (UNUSED)
- Line 24: unused variable 'valid_mean_token_accuracy' (60% confidence) (UNUSED)
- Line 31: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 46: unused variable 'step_number' (60% confidence) (UNUSED)

#### reinforcement_hyperparameters.py
- Line 19: unused variable 'compute_multiplier' (60% confidence) (UNUSED)
- Line 24: unused variable 'eval_interval' (60% confidence) (UNUSED)
- Line 27: unused variable 'eval_samples' (60% confidence) (UNUSED)
- Line 30: unused variable 'learning_rate_multiplier' (60% confidence) (UNUSED)
- Line 36: unused variable 'n_epochs' (60% confidence) (UNUSED)

#### reinforcement_hyperparameters_param.py
- Line 19: unused variable 'compute_multiplier' (60% confidence) (UNUSED)
- Line 24: unused variable 'eval_interval' (60% confidence) (UNUSED)
- Line 27: unused variable 'eval_samples' (60% confidence) (UNUSED)
- Line 30: unused variable 'learning_rate_multiplier' (60% confidence) (UNUSED)
- Line 36: unused variable 'n_epochs' (60% confidence) (UNUSED)

#### supervised_hyperparameters.py
- Line 19: unused variable 'learning_rate_multiplier' (60% confidence) (UNUSED)
- Line 25: unused variable 'n_epochs' (60% confidence) (UNUSED)

#### supervised_hyperparameters_param.py
- Line 19: unused variable 'learning_rate_multiplier' (60% confidence) (UNUSED)
- Line 25: unused variable 'n_epochs' (60% confidence) (UNUSED)

#### label_model_grader.py
- Line 49: unused variable 'passing_labels' (60% confidence) (UNUSED)

#### label_model_grader_param.py
- Line 50: unused variable 'passing_labels' (60% confidence) (UNUSED)

#### multi_grader.py
- Line 19: unused variable 'calculate_output' (60% confidence) (UNUSED)

#### multi_grader_param.py
- Line 22: unused variable 'calculate_output' (60% confidence) (UNUSED)

#### python_grader.py
- Line 21: unused variable 'image_tag' (60% confidence) (UNUSED)

#### python_grader_param.py
- Line 20: unused variable 'image_tag' (60% confidence) (UNUSED)

#### score_model_grader.py
- Line 53: unused variable 'sampling_params' (60% confidence) (UNUSED)

#### score_model_grader_param.py
- Line 54: unused variable 'sampling_params' (60% confidence) (UNUSED)

#### text_similarity_grader.py
- Line 11: unused variable 'evaluation_metric' (60% confidence) (UNUSED)

#### text_similarity_grader_param.py
- Line 11: unused variable 'evaluation_metric' (60% confidence) (UNUSED)

#### image.py
- Line 11: unused variable 'b64_json' (60% confidence) (UNUSED)
- Line 18: unused variable 'revised_prompt' (60% confidence) (UNUSED)

#### images_response.py
- Line 12: unused variable 'image_tokens' (60% confidence) (UNUSED)
- Line 15: unused variable 'text_tokens' (60% confidence) (UNUSED)
- Line 20: unused variable 'input_tokens' (60% confidence) (UNUSED)
- Line 23: unused variable 'input_tokens_details' (60% confidence) (UNUSED)
- Line 26: unused variable 'output_tokens' (60% confidence) (UNUSED)

#### model.py
- Line 20: unused variable 'owned_by' (60% confidence) (UNUSED)

#### moderation.py
- Line 14: unused variable 'harassment' (60% confidence) (UNUSED)
- Line 20: unused variable 'harassment_threatening' (60% confidence) (UNUSED)
- Line 26: unused variable 'hate' (60% confidence) (UNUSED)
- Line 34: unused variable 'hate_threatening' (60% confidence) (UNUSED)
- Line 41: unused variable 'illicit' (60% confidence) (UNUSED)
- Line 48: unused variable 'illicit_violent' (60% confidence) (UNUSED)
- Line 55: unused variable 'self_harm' (60% confidence) (UNUSED)
- Line 61: unused variable 'self_harm_instructions' (60% confidence) (UNUSED)
- Line 68: unused variable 'self_harm_intent' (60% confidence) (UNUSED)
- Line 74: unused variable 'sexual' (60% confidence) (UNUSED)
- Line 81: unused variable 'sexual_minors' (60% confidence) (UNUSED)
- Line 84: unused variable 'violence' (60% confidence) (UNUSED)
- Line 87: unused variable 'violence_graphic' (60% confidence) (UNUSED)
- Line 92: unused variable 'harassment' (60% confidence) (UNUSED)
- Line 95: unused variable 'harassment_threatening' (60% confidence) (UNUSED)
- Line 98: unused variable 'hate' (60% confidence) (UNUSED)
- Line 101: unused variable 'hate_threatening' (60% confidence) (UNUSED)
- Line 104: unused variable 'illicit' (60% confidence) (UNUSED)
- Line 107: unused variable 'illicit_violent' (60% confidence) (UNUSED)
- Line 110: unused variable 'self_harm' (60% confidence) (UNUSED)
- Line 113: unused variable 'self_harm_instructions' (60% confidence) (UNUSED)
- Line 116: unused variable 'self_harm_intent' (60% confidence) (UNUSED)
- Line 119: unused variable 'sexual' (60% confidence) (UNUSED)
- Line 122: unused variable 'sexual_minors' (60% confidence) (UNUSED)
- Line 125: unused variable 'violence' (60% confidence) (UNUSED)
- Line 128: unused variable 'violence_graphic' (60% confidence) (UNUSED)
- Line 133: unused variable 'harassment' (60% confidence) (UNUSED)
- Line 136: unused variable 'harassment_threatening' (60% confidence) (UNUSED)
- Line 139: unused variable 'hate' (60% confidence) (UNUSED)
- Line 142: unused variable 'hate_threatening' (60% confidence) (UNUSED)
- Line 145: unused variable 'illicit' (60% confidence) (UNUSED)
- Line 148: unused variable 'illicit_violent' (60% confidence) (UNUSED)
- Line 151: unused variable 'self_harm' (60% confidence) (UNUSED)
- Line 154: unused variable 'self_harm_instructions' (60% confidence) (UNUSED)
- Line 157: unused variable 'self_harm_intent' (60% confidence) (UNUSED)
- Line 160: unused variable 'sexual' (60% confidence) (UNUSED)
- Line 163: unused variable 'sexual_minors' (60% confidence) (UNUSED)
- Line 166: unused variable 'violence' (60% confidence) (UNUSED)
- Line 169: unused variable 'violence_graphic' (60% confidence) (UNUSED)
- Line 177: unused variable 'category_applied_input_types' (60% confidence) (UNUSED)
- Line 182: unused variable 'category_scores' (60% confidence) (UNUSED)

#### file_search_tool.py
- Line 19: unused variable 'score_threshold' (60% confidence) (UNUSED)
- Line 31: unused variable 'vector_store_ids' (60% confidence) (UNUSED)

#### file_search_tool_param.py
- Line 20: unused variable 'score_threshold' (60% confidence) (UNUSED)
- Line 32: unused variable 'vector_store_ids' (60% confidence) (UNUSED)

#### parsed_response.py
- Line 69: unused property 'output_parsed' (60% confidence) (UNUSED)

#### response.py
- Line 35: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 41: unused variable 'incomplete_details' (60% confidence) (UNUSED)
- Line 211: unused property 'output_text' (60% confidence) (UNUSED)

#### response_code_interpreter_call_completed_event.py
- Line 12: unused variable 'code_interpreter_call' (60% confidence) (UNUSED)

#### response_code_interpreter_call_in_progress_event.py
- Line 12: unused variable 'code_interpreter_call' (60% confidence) (UNUSED)

#### response_code_interpreter_call_interpreting_event.py
- Line 12: unused variable 'code_interpreter_call' (60% confidence) (UNUSED)

#### response_computer_tool_call.py
- Line 126: unused variable 'scroll_x' (60% confidence) (UNUSED)
- Line 129: unused variable 'scroll_y' (60% confidence) (UNUSED)
- Line 198: unused variable 'call_id' (60% confidence) (UNUSED)
- Line 201: unused variable 'pending_safety_checks' (60% confidence) (UNUSED)

#### response_computer_tool_call_output_item.py
- Line 27: unused variable 'call_id' (60% confidence) (UNUSED)
- Line 36: unused variable 'acknowledged_safety_checks' (60% confidence) (UNUSED)

#### response_computer_tool_call_param.py
- Line 125: unused variable 'scroll_x' (60% confidence) (UNUSED)
- Line 128: unused variable 'scroll_y' (60% confidence) (UNUSED)
- Line 194: unused variable 'call_id' (60% confidence) (UNUSED)
- Line 197: unused variable 'pending_safety_checks' (60% confidence) (UNUSED)

#### response_file_search_tool_call.py
- Line 38: unused variable 'queries' (60% confidence) (UNUSED)

#### response_file_search_tool_call_param.py
- Line 38: unused variable 'queries' (60% confidence) (UNUSED)

#### response_function_tool_call.py
- Line 15: unused variable 'call_id' (60% confidence) (UNUSED)

#### response_function_tool_call_output_item.py
- Line 15: unused variable 'call_id' (60% confidence) (UNUSED)

#### response_function_tool_call_param.py
- Line 14: unused variable 'call_id' (60% confidence) (UNUSED)

#### response_input_item_param.py
- Line 61: unused variable 'call_id' (60% confidence) (UNUSED)
- Line 73: unused variable 'acknowledged_safety_checks' (60% confidence) (UNUSED)
- Line 88: unused variable 'call_id' (60% confidence) (UNUSED)

#### response_input_param.py
- Line 62: unused variable 'call_id' (60% confidence) (UNUSED)
- Line 74: unused variable 'acknowledged_safety_checks' (60% confidence) (UNUSED)
- Line 89: unused variable 'call_id' (60% confidence) (UNUSED)

#### response_item_list.py
- Line 16: unused variable 'first_id' (60% confidence) (UNUSED)
- Line 22: unused variable 'last_id' (60% confidence) (UNUSED)

#### response_reasoning_item.py
- Line 31: unused variable 'encrypted_content' (60% confidence) (UNUSED)

#### response_reasoning_item_param.py
- Line 31: unused variable 'encrypted_content' (60% confidence) (UNUSED)

#### response_reasoning_summary_part_added_event.py
- Line 28: unused variable 'summary_index' (60% confidence) (UNUSED)

#### response_reasoning_summary_part_done_event.py
- Line 28: unused variable 'summary_index' (60% confidence) (UNUSED)

#### response_reasoning_summary_text_delta_event.py
- Line 20: unused variable 'summary_index' (60% confidence) (UNUSED)

#### response_reasoning_summary_text_done_event.py
- Line 17: unused variable 'summary_index' (60% confidence) (UNUSED)

#### response_text_annotation_delta_event.py
- Line 66: unused variable 'annotation_index' (60% confidence) (UNUSED)

#### response_usage.py
- Line 9: unused variable 'cached_tokens' (60% confidence) (UNUSED)
- Line 17: unused variable 'reasoning_tokens' (60% confidence) (UNUSED)
- Line 22: unused variable 'input_tokens' (60% confidence) (UNUSED)
- Line 25: unused variable 'input_tokens_details' (60% confidence) (UNUSED)
- Line 28: unused variable 'output_tokens' (60% confidence) (UNUSED)
- Line 31: unused variable 'output_tokens_details' (60% confidence) (UNUSED)

#### web_search_tool.py
- Line 15: unused variable 'city' (60% confidence) (UNUSED)
- Line 18: unused variable 'country' (60% confidence) (UNUSED)
- Line 41: unused variable 'search_context_size' (60% confidence) (UNUSED)
- Line 48: unused variable 'user_location' (60% confidence) (UNUSED)

#### web_search_tool_param.py
- Line 15: unused variable 'city' (60% confidence) (UNUSED)
- Line 18: unused variable 'country' (60% confidence) (UNUSED)
- Line 41: unused variable 'search_context_size' (60% confidence) (UNUSED)
- Line 48: unused variable 'user_location' (60% confidence) (UNUSED)

#### reasoning.py
- Line 13: unused variable 'effort' (60% confidence) (UNUSED)

#### reasoning.py
- Line 14: unused variable 'effort' (60% confidence) (UNUSED)

#### static_file_chunking_strategy.py
- Line 9: unused variable 'chunk_overlap_tokens' (60% confidence) (UNUSED)
- Line 15: unused variable 'max_chunk_size_tokens' (60% confidence) (UNUSED)

#### static_file_chunking_strategy_param.py
- Line 11: unused variable 'chunk_overlap_tokens' (60% confidence) (UNUSED)
- Line 17: unused variable 'max_chunk_size_tokens' (60% confidence) (UNUSED)

#### upload.py
- Line 19: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 22: unused variable 'expires_at' (60% confidence) (UNUSED)

#### upload_part.py
- Line 14: unused variable 'created_at' (60% confidence) (UNUSED)

#### vector_store.py
- Line 44: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 49: unused variable 'last_active_at' (60% confidence) (UNUSED)
- Line 75: unused variable 'usage_bytes' (60% confidence) (UNUSED)
- Line 81: unused variable 'expires_at' (60% confidence) (UNUSED)

#### vector_store_search_params.py
- Line 40: unused variable 'score_threshold' (60% confidence) (UNUSED)

#### vector_store_file.py
- Line 24: unused variable 'created_at' (60% confidence) (UNUSED)
- Line 43: unused variable 'usage_bytes' (60% confidence) (UNUSED)

#### vector_store_file_batch.py
- Line 31: unused variable 'created_at' (60% confidence) (UNUSED)

#### websocket_connection_options.py
- Line 32: unused variable 'max_queue' (60% confidence) (UNUSED)
- Line 35: unused variable 'write_limit' (60% confidence) (UNUSED)

#### _elffile.py
- Line 25: unused variable 'C64' (60% confidence) (UNUSED)
- Line 30: unused variable 'Msb' (60% confidence) (UNUSED)
- Line 35: unused variable 'S390' (60% confidence) (UNUSED)
- Line 37: unused variable 'X8664' (60% confidence) (UNUSED)
- Line 38: unused variable 'AArc64' (60% confidence) (UNUSED)

#### markers.py
- Line 65: unused variable 'platform_machine' (60% confidence) (UNUSED)
- Line 72: unused variable 'platform_release' (60% confidence) (UNUSED)
- Line 79: unused variable 'platform_system' (60% confidence) (UNUSED)
- Line 86: unused variable 'platform_version' (60% confidence) (UNUSED)
- Line 93: unused variable 'python_full_version' (60% confidence) (UNUSED)
- Line 101: unused variable 'platform_python_implementation' (60% confidence) (UNUSED)
- Line 109: unused variable 'sys_platform' (60% confidence) (UNUSED)

#### metadata.py
- Line 88: unused variable 'home_page' (60% confidence) (UNUSED)
- Line 94: unused variable 'supported_platforms' (60% confidence) (UNUSED)
- Line 104: unused variable 'requires_dist' (60% confidence) (UNUSED)
- Line 105: unused variable 'provides_dist' (60% confidence) (UNUSED)
- Line 106: unused variable 'obsoletes_dist' (60% confidence) (UNUSED)
- Line 108: unused variable 'requires_external' (60% confidence) (UNUSED)
- Line 121: unused variable 'description_content_type' (60% confidence) (UNUSED)
- Line 122: unused variable 'provides_extra' (60% confidence) (UNUSED)
- Line 533: unused method '_process_metadata_version' (60% confidence) (UNUSED)
- Line 539: unused method '_process_name' (60% confidence) (UNUSED)
- Line 552: unused method '_process_version' (60% confidence) (UNUSED)
- Line 562: unused method '_process_summary' (60% confidence) (UNUSED)
- Line 568: unused method '_process_description_content_type' (60% confidence) (UNUSED)
- Line 600: unused method '_process_dynamic' (60% confidence) (UNUSED)
- Line 612: unused method '_process_provides_extra' (60% confidence) (UNUSED)
- Line 627: unused method '_process_requires_python' (60% confidence) (UNUSED)
- Line 635: unused method '_process_requires_dist' (60% confidence) (UNUSED)
- Line 650: unused method '_process_license_expression' (60% confidence) (UNUSED)
- Line 660: unused method '_process_license_files' (60% confidence) (UNUSED)
- Line 756: unused method 'from_email' (60% confidence) (UNUSED)
- Line 802: unused variable 'supported_platforms' (60% confidence) (UNUSED)
- Line 808: unused variable 'description_content_type' (60% confidence) (UNUSED)
- Line 812: unused variable 'home_page' (60% confidence) (UNUSED)
- Line 834: unused variable 'requires_dist' (60% confidence) (UNUSED)
- Line 844: unused variable 'requires_external' (60% confidence) (UNUSED)
- Line 850: unused variable 'provides_extra' (60% confidence) (UNUSED)
- Line 854: unused variable 'provides_dist' (60% confidence) (UNUSED)
- Line 856: unused variable 'obsoletes_dist' (60% confidence) (UNUSED)

#### specifiers.py
- Line 368: unused method '_compare_compatible' (60% confidence) (UNUSED)
- Line 428: unused method '_compare_not_equal' (60% confidence) (UNUSED)
- Line 431: unused method '_compare_less_than_equal' (60% confidence) (UNUSED)
- Line 437: unused method '_compare_greater_than_equal' (60% confidence) (UNUSED)
- Line 443: unused method '_compare_less_than' (60% confidence) (UNUSED)
- Line 467: unused method '_compare_greater_than' (60% confidence) (UNUSED)
- Line 497: unused method '_compare_arbitrary' (60% confidence) (UNUSED)

#### utils.py
- Line 54: unused function 'is_normalized_name' (60% confidence) (UNUSED)

#### version.py
- Line 35: unused variable 'VersionComparisonMethod' (60% confidence) (UNUSED)
- Line 411: unused property 'is_devrelease' (60% confidence) (UNUSED)

#### __init__.py
- Line 50: unused function 'using_nullable_dtypes' (60% confidence) (UNUSED)

#### _typing.py
- Line 166: unused variable 'TimestampNonexistent' (60% confidence) (UNUSED)
- Line 268: unused variable '__whence' (100% confidence) (UNUSED)
- Line 283: unused variable '__n' (100% confidence) (UNUSED)
- Line 289: unused variable '__b' (100% confidence) (UNUSED)
- Line 516: unused variable 'OffsetCalendar' (60% confidence) (UNUSED)

#### _version.py
- Line 44: unused attribute 'VCS' (60% confidence) (UNUSED)
- Line 57: unused variable 'LONG_VERSION_PY' (60% confidence) (UNUSED)
- Line 83: unused attribute 'dwFlags' (60% confidence) (UNUSED)
- Line 150: unused function 'git_get_keywords' (60% confidence) (UNUSED)

#### __init__.py
- Line 29: unused variable 'np_ulong' (60% confidence) (UNUSED)
- Line 40: unused variable 'np_ulong' (60% confidence) (UNUSED)
- Line 43: unused variable 'np_ulong' (60% confidence) (UNUSED)
- Line 46: unused variable 'np_ulong' (60% confidence) (UNUSED)

#### function.py
- Line 263: unused variable 'validate_reshape' (60% confidence) (UNUSED)
- Line 281: unused variable 'validate_sort' (60% confidence) (UNUSED)
- Line 328: unused function 'validate_take_with_convert' (60% confidence) (UNUSED)

#### conftest.py
- Line 111: unused function 'pytest_addoption' (60% confidence) (UNUSED)
- Line 137: unused function 'pytest_collection_modifyitems' (60% confidence) (UNUSED)
- Line 256: unused function 'add_doctest_imports' (60% confidence) (UNUSED)
- Line 265: unused function 'configure_tests' (60% confidence) (UNUSED)
- Line 678: unused variable 'index_fixture2' (60% confidence) (UNUSED)
- Line 1186: unused variable 'tz_aware_fixture2' (60% confidence) (UNUSED)
- Line 1822: unused attribute 'hist_file' (60% confidence) (UNUSED)

#### extensions.py
- Line 125: unused function 'typeof_index' (60% confidence) (UNUSED)
- Line 138: unused function 'typeof_series' (60% confidence) (UNUSED)
- Line 148: unused function 'type_series_constructor' (60% confidence) (UNUSED)
- Line 160: unused function 'type_index_constructor' (60% confidence) (UNUSED)
- Line 173: unused class 'IndexModel' (60% confidence) (UNUSED)
- Line 191: unused class 'SeriesModel' (60% confidence) (UNUSED)
- Line 210: unused function 'pdseries_constructor' (60% confidence) (UNUSED)
- Line 220: unused function 'pdseries_constructor_with_name' (60% confidence) (UNUSED)
- Line 232: unused function 'index_constructor_2arg' (60% confidence) (UNUSED)
- Line 243: unused function 'index_constructor_2arg_parent' (60% confidence) (UNUSED)
- Line 255: unused function 'index_constructor_1arg' (60% confidence) (UNUSED)
- Line 275: unused function 'maybe_cast_str_impl' (60% confidence) (UNUSED)
- Line 285: unused function 'unbox_index' (60% confidence) (UNUSED)
- Line 318: unused function 'unbox_series' (60% confidence) (UNUSED)
- Line 340: unused function 'box_index' (60% confidence) (UNUSED)
- Line 385: unused function 'box_series' (60% confidence) (UNUSED)
- Line 489: unused function 'index_get_loc' (60% confidence) (UNUSED)
- Line 502: unused function 'series_indexing' (60% confidence) (UNUSED)
- Line 513: unused function 'index_indexing' (60% confidence) (UNUSED)
- Line 534: unused function 'typeof_iloc' (60% confidence) (UNUSED)
- Line 540: unused function 'type_iloc_constructor' (60% confidence) (UNUSED)
- Line 549: unused function 'iloc_constructor' (60% confidence) (UNUSED)
- Line 559: unused class 'ILocModel' (60% confidence) (UNUSED)
- Line 569: unused function 'series_iloc' (60% confidence) (UNUSED)
- Line 577: unused function 'iloc_getitem' (60% confidence) (UNUSED)

#### array.py
- Line 2406: unused method '_str_isalnum' (60% confidence) (UNUSED)
- Line 2409: unused method '_str_isalpha' (60% confidence) (UNUSED)
- Line 2412: unused method '_str_isdecimal' (60% confidence) (UNUSED)
- Line 2415: unused method '_str_isdigit' (60% confidence) (UNUSED)
- Line 2418: unused method '_str_islower' (60% confidence) (UNUSED)
- Line 2421: unused method '_str_isnumeric' (60% confidence) (UNUSED)
- Line 2424: unused method '_str_isspace' (60% confidence) (UNUSED)
- Line 2427: unused method '_str_istitle' (60% confidence) (UNUSED)
- Line 2430: unused method '_str_isupper' (60% confidence) (UNUSED)
- Line 2581: unused property '_dt_days' (60% confidence) (UNUSED)
- Line 2587: unused property '_dt_hours' (60% confidence) (UNUSED)
- Line 2599: unused property '_dt_minutes' (60% confidence) (UNUSED)
- Line 2611: unused property '_dt_seconds' (60% confidence) (UNUSED)
- Line 2619: unused property '_dt_milliseconds' (60% confidence) (UNUSED)
- Line 2631: unused property '_dt_microseconds' (60% confidence) (UNUSED)
- Line 2641: unused property '_dt_nanoseconds' (60% confidence) (UNUSED)
- Line 2655: unused method '_dt_total_seconds' (60% confidence) (UNUSED)
- Line 2660: unused method '_dt_as_unit' (60% confidence) (UNUSED)
- Line 2667: unused property '_dt_year' (60% confidence) (UNUSED)
- Line 2671: unused property '_dt_day' (60% confidence) (UNUSED)
- Line 2688: unused property '_dt_hour' (60% confidence) (UNUSED)
- Line 2695: unused property '_dt_is_leap_year' (60% confidence) (UNUSED)
- Line 2699: unused property '_dt_is_month_start' (60% confidence) (UNUSED)
- Line 2703: unused property '_dt_is_month_end' (60% confidence) (UNUSED)
- Line 2714: unused property '_dt_is_year_start' (60% confidence) (UNUSED)
- Line 2723: unused property '_dt_is_year_end' (60% confidence) (UNUSED)
- Line 2732: unused property '_dt_is_quarter_start' (60% confidence) (UNUSED)
- Line 2740: unused property '_dt_is_quarter_end' (60% confidence) (UNUSED)
- Line 2761: unused property '_dt_microsecond' (60% confidence) (UNUSED)
- Line 2765: unused property '_dt_minute' (60% confidence) (UNUSED)
- Line 2769: unused property '_dt_month' (60% confidence) (UNUSED)
- Line 2773: unused property '_dt_nanosecond' (60% confidence) (UNUSED)
- Line 2777: unused property '_dt_quarter' (60% confidence) (UNUSED)
- Line 2781: unused property '_dt_second' (60% confidence) (UNUSED)
- Line 2785: unused property '_dt_date' (60% confidence) (UNUSED)
- Line 2789: unused property '_dt_time' (60% confidence) (UNUSED)
- Line 2798: unused property '_dt_tz' (60% confidence) (UNUSED)
- Line 2802: unused property '_dt_unit' (60% confidence) (UNUSED)
- Line 2806: unused method '_dt_normalize' (60% confidence) (UNUSED)
- Line 2809: unused method '_dt_strftime' (60% confidence) (UNUSED)
- Line 2849: unused method '_dt_ceil' (60% confidence) (UNUSED)
- Line 2857: unused method '_dt_floor' (60% confidence) (UNUSED)
- Line 2865: unused method '_dt_round' (60% confidence) (UNUSED)
- Line 2873: unused method '_dt_day_name' (60% confidence) (UNUSED)
- Line 2878: unused method '_dt_month_name' (60% confidence) (UNUSED)

#### base.py
- Line 2452: unused method '_add_comparison_ops' (60% confidence) (UNUSED)
- Line 2465: unused method '_add_logical_ops' (60% confidence) (UNUSED)

#### datetimes.py
- Line 758: unused method '_has_same_tz' (60% confidence) (UNUSED)

#### interval.py
- Line 214: unused variable 'can_hold_na' (60% confidence) (UNUSED)

#### array.py
- Line 670: unused method '_fill_value_matches' (60% confidence) (UNUSED)

#### string_arrow.py
- Line 68: unused variable 'ArrowStringScalarOrNAT' (60% confidence) (UNUSED)
- Line 455: unused method '_str_isalnum' (60% confidence) (UNUSED)
- Line 459: unused method '_str_isalpha' (60% confidence) (UNUSED)
- Line 463: unused method '_str_isdecimal' (60% confidence) (UNUSED)
- Line 467: unused method '_str_isdigit' (60% confidence) (UNUSED)
- Line 471: unused method '_str_islower' (60% confidence) (UNUSED)
- Line 475: unused method '_str_isnumeric' (60% confidence) (UNUSED)
- Line 479: unused method '_str_isspace' (60% confidence) (UNUSED)
- Line 483: unused method '_str_istitle' (60% confidence) (UNUSED)
- Line 487: unused method '_str_isupper' (60% confidence) (UNUSED)

#### expr.py
- Line 381: unused variable 'unary_op_nodes_map' (60% confidence) (UNUSED)

#### config_init.py
- Line 97: unused variable 'pc_colspace_doc' (60% confidence) (UNUSED)
- Line 207: unused variable 'pc_ambiguous_as_wide_doc' (60% confidence) (UNUSED)

#### cast.py
- Line 120: unused variable 'NumpyArrayT' (60% confidence) (UNUSED)
- Line 606: unused variable 'fill_value_type' (100% confidence) (UNUSED)

#### generic.py
- Line 131: unused variable 'ABCPeriodArray' (60% confidence) (UNUSED)

#### generic.py
- Line 121: unused variable 'ScalarResult' (60% confidence) (UNUSED)

#### groupby.py
- Line 1857: unused variable 'is_agg' (100% confidence) (UNUSED)

#### grouper.py
- Line 708: unused property 'group_arraylike' (60% confidence) (UNUSED)

#### multi.py
- Line 136: unused method '_codes_to_ints' (60% confidence) (UNUSED)
- Line 176: unused method '_codes_to_ints' (60% confidence) (UNUSED)
- Line 2575: unused method '_recode_for_new_levels' (60% confidence) (UNUSED)

#### dataframe_protocol.py
- Line 30: unused variable 'CPU_PINNED' (60% confidence) (UNUSED)
- Line 31: unused variable 'OPENCL' (60% confidence) (UNUSED)
- Line 32: unused variable 'VULKAN' (60% confidence) (UNUSED)
- Line 33: unused variable 'METAL' (60% confidence) (UNUSED)
- Line 34: unused variable 'VPI' (60% confidence) (UNUSED)
- Line 35: unused variable 'ROCM' (60% confidence) (UNUSED)
- Line 113: unused variable 'is_ordered' (60% confidence) (UNUSED)

#### utils.py
- Line 71: unused variable 'INT8' (60% confidence) (UNUSED)
- Line 73: unused variable 'INT16' (60% confidence) (UNUSED)
- Line 74: unused variable 'UINT16' (60% confidence) (UNUSED)
- Line 75: unused variable 'INT32' (60% confidence) (UNUSED)
- Line 76: unused variable 'UINT32' (60% confidence) (UNUSED)
- Line 78: unused variable 'UINT64' (60% confidence) (UNUSED)
- Line 79: unused variable 'FLOAT16' (60% confidence) (UNUSED)
- Line 80: unused variable 'FLOAT32' (60% confidence) (UNUSED)
- Line 81: unused variable 'FLOAT64' (60% confidence) (UNUSED)
- Line 84: unused variable 'DATE32' (60% confidence) (UNUSED)
- Line 85: unused variable 'DATE64' (60% confidence) (UNUSED)
- Line 98: unused variable 'LITTLE' (60% confidence) (UNUSED)
- Line 99: unused variable 'BIG' (60% confidence) (UNUSED)

#### array_manager.py
- Line 700: unused property 'column_arrays' (60% confidence) (UNUSED)

#### blocks.py
- Line 2521: unused method 'slice_block_rows' (60% confidence) (UNUSED)

#### managers.py
- Line 1038: unused property 'column_arrays' (60% confidence) (UNUSED)

#### describe.py
- Line 260: unused variable 'percentiles_ignored' (100% confidence) (UNUSED)
- Line 290: unused function 'describe_timestamp_as_categorical_1d' (60% confidence) (UNUSED)
- Line 292: unused variable 'percentiles_ignored' (100% confidence) (UNUSED)

#### missing.py
- Line 805: unused function '_interpolate_with_limit_area' (60% confidence) (UNUSED)

#### base.py
- Line 166: unused method '_str_isalnum' (60% confidence) (UNUSED)
- Line 170: unused method '_str_isalpha' (60% confidence) (UNUSED)
- Line 174: unused method '_str_isdecimal' (60% confidence) (UNUSED)
- Line 178: unused method '_str_isdigit' (60% confidence) (UNUSED)
- Line 182: unused method '_str_islower' (60% confidence) (UNUSED)
- Line 186: unused method '_str_isnumeric' (60% confidence) (UNUSED)
- Line 190: unused method '_str_isspace' (60% confidence) (UNUSED)
- Line 194: unused method '_str_istitle' (60% confidence) (UNUSED)
- Line 198: unused method '_str_isupper' (60% confidence) (UNUSED)

#### object_array.py
- Line 404: unused method '_str_isalnum' (60% confidence) (UNUSED)
- Line 407: unused method '_str_isalpha' (60% confidence) (UNUSED)
- Line 410: unused method '_str_isdecimal' (60% confidence) (UNUSED)
- Line 413: unused method '_str_isdigit' (60% confidence) (UNUSED)
- Line 416: unused method '_str_islower' (60% confidence) (UNUSED)
- Line 419: unused method '_str_isnumeric' (60% confidence) (UNUSED)
- Line 422: unused method '_str_isspace' (60% confidence) (UNUSED)
- Line 425: unused method '_str_istitle' (60% confidence) (UNUSED)
- Line 428: unused method '_str_isupper' (60% confidence) (UNUSED)

#### _openpyxl.py
- Line 180: unused method '_convert_to_font' (60% confidence) (UNUSED)
- Line 246: unused method '_convert_to_fill' (60% confidence) (UNUSED)
- Line 342: unused method '_convert_to_border' (60% confidence) (UNUSED)
- Line 382: unused method '_convert_to_alignment' (60% confidence) (UNUSED)
- Line 405: unused method '_convert_to_number_format' (60% confidence) (UNUSED)
- Line 423: unused method '_convert_to_protection' (60% confidence) (UNUSED)

#### excel.py
- Line 410: unused method '_get_underline' (60% confidence) (UNUSED)

#### format.py
- Line 522: unused property 'max_rows_displayed' (60% confidence) (UNUSED)

#### printing.py
- Line 266: unused variable 'print_method' (60% confidence) (UNUSED)

#### style.py
- Line 1986: unused method 'applymap_index' (60% confidence) (UNUSED)
- Line 2981: unused method 'text_gradient' (60% confidence) (UNUSED)

#### readers.py
- Line 507: unused class '_DeprecationConfig' (60% confidence) (UNUSED)
- Line 1904: unused method '_failover_to_python' (60% confidence) (UNUSED)

#### pytables.py
- Line 2108: unused attribute '_v_pos' (60% confidence) (UNUSED)
- Line 3519: unused property 'data_orientation' (60% confidence) (UNUSED)

#### sas7bdat.py
- Line 204: unused attribute '_current_row_on_page_index' (60% confidence) (UNUSED)
- Line 233: unused method 'column_data_lengths' (60% confidence) (UNUSED)
- Line 237: unused method 'column_data_offsets' (60% confidence) (UNUSED)
- Line 299: unused attribute 'date_created' (60% confidence) (UNUSED)
- Line 303: unused attribute 'date_modified' (60% confidence) (UNUSED)
- Line 371: unused method '_read_and_convert_header_text' (60% confidence) (UNUSED)
- Line 406: unused attribute '_current_page_block_count' (60% confidence) (UNUSED)
- Line 466: unused attribute 'row_length' (60% confidence) (UNUSED)
- Line 481: unused attribute '_mix_page_row_count' (60% confidence) (UNUSED)

#### sas_constants.py
- Line 15: unused variable 'align_1_value' (60% confidence) (UNUSED)
- Line 22: unused variable 'platform_offset' (60% confidence) (UNUSED)
- Line 23: unused variable 'platform_length' (60% confidence) (UNUSED)
- Line 26: unused variable 'dataset_offset' (60% confidence) (UNUSED)
- Line 27: unused variable 'dataset_length' (60% confidence) (UNUSED)
- Line 28: unused variable 'file_type_offset' (60% confidence) (UNUSED)
- Line 29: unused variable 'file_type_length' (60% confidence) (UNUSED)
- Line 38: unused variable 'page_count_offset' (60% confidence) (UNUSED)
- Line 39: unused variable 'page_count_length' (60% confidence) (UNUSED)
- Line 40: unused variable 'sas_release_offset' (60% confidence) (UNUSED)
- Line 41: unused variable 'sas_release_length' (60% confidence) (UNUSED)
- Line 42: unused variable 'sas_server_type_offset' (60% confidence) (UNUSED)
- Line 43: unused variable 'sas_server_type_length' (60% confidence) (UNUSED)
- Line 44: unused variable 'os_version_number_offset' (60% confidence) (UNUSED)
- Line 45: unused variable 'os_version_number_length' (60% confidence) (UNUSED)
- Line 46: unused variable 'os_maker_offset' (60% confidence) (UNUSED)
- Line 47: unused variable 'os_maker_length' (60% confidence) (UNUSED)
- Line 48: unused variable 'os_name_offset' (60% confidence) (UNUSED)
- Line 49: unused variable 'os_name_length' (60% confidence) (UNUSED)
- Line 68: unused variable 'page_comp_type' (60% confidence) (UNUSED)
- Line 180: unused variable 'data_subheader_index' (60% confidence) (UNUSED)
- Line 183: unused variable 'subheader_signature_to_index' (60% confidence) (UNUSED)

#### sql.py
- Line 2053: unused attribute 'asdecimal' (60% confidence) (UNUSED)

#### stata.py
- Line 1160: unused attribute '_missing_values' (60% confidence) (UNUSED)
- Line 1161: unused attribute '_can_read_value_labels' (60% confidence) (UNUSED)
- Line 1164: unused attribute '_data_read' (60% confidence) (UNUSED)
- Line 1333: unused attribute '_srtlist' (60% confidence) (UNUSED)
- Line 1456: unused attribute '_filetype' (60% confidence) (UNUSED)
- Line 1498: unused attribute '_srtlist' (60% confidence) (UNUSED)
- Line 1707: unused attribute '_can_read_value_labels' (60% confidence) (UNUSED)
- Line 1708: unused attribute '_data_read' (60% confidence) (UNUSED)
- Line 1721: unused attribute '_can_read_value_labels' (60% confidence) (UNUSED)
- Line 1745: unused attribute '_can_read_value_labels' (60% confidence) (UNUSED)
- Line 1746: unused attribute '_data_read' (60% confidence) (UNUSED)
- Line 2372: unused attribute 'type_converters' (60% confidence) (UNUSED)
- Line 3061: unused attribute '_dta_ver' (60% confidence) (UNUSED)

#### xml.py
- Line 179: unused attribute 'is_style' (60% confidence) (UNUSED)

#### converter.py
- Line 173: unused method 'axisinfo' (60% confidence) (UNUSED)
- Line 182: unused method 'default_units' (60% confidence) (UNUSED)
- Line 334: unused method 'axisinfo' (60% confidence) (UNUSED)
- Line 450: unused method 'autoscale' (60% confidence) (UNUSED)
- Line 1015: unused method 'autoscale' (60% confidence) (UNUSED)
- Line 1082: unused method 'set_locs' (60% confidence) (UNUSED)

#### test_indexing.py
- Line 363: unused function 'non_coercible_categorical' (60% confidence) (UNUSED)

#### test_eval.py
- Line 282: unused variable 'ghs' (60% confidence) (UNUSED)

#### test_config.py
- Line 11: unused method 'clean_config' (60% confidence) (UNUSED)

#### test_generic.py
- Line 125: unused attribute 'not_an_index' (60% confidence) (UNUSED)

#### dim2.py
- Line 23: unused method 'skip_if_doesnt_support_2d' (60% confidence) (UNUSED)

#### setitem.py
- Line 38: unused method 'skip_if_immutable' (60% confidence) (UNUSED)

#### test_numpy.py
- Line 53: unused function 'allow_in_pandas' (60% confidence) (UNUSED)
- Line 77: unused variable 'allow_in_pandas' (100% confidence) (UNUSED)
- Line 84: unused variable 'allow_in_pandas' (100% confidence) (UNUSED)
- Line 99: unused variable 'allow_in_pandas' (100% confidence) (UNUSED)
- Line 113: unused variable 'allow_in_pandas' (100% confidence) (UNUSED)
- Line 125: unused variable 'allow_in_pandas' (100% confidence) (UNUSED)
- Line 149: unused function 'skip_numpy_object' (60% confidence) (UNUSED)

#### test_string.py
- Line 222: unused method 'arrow_not_supported' (60% confidence) (UNUSED)

#### test_where.py
- Line 825: unused variable 'where_res' (60% confidence) (UNUSED)
- Line 826: unused variable 'where_res' (60% confidence) (UNUSED)
- Line 830: unused variable 'where_res' (60% confidence) (UNUSED)
- Line 831: unused variable 'where_res' (60% confidence) (UNUSED)

#### test_info.py
- Line 26: unused function 'duplicate_columns_frame' (60% confidence) (UNUSED)

#### test_value_counts.py
- Line 28: unused function 'tests_value_counts_index_names_category_column' (60% confidence) (UNUSED)

#### test_groupby.py
- Line 1295: unused variable 'sorted_columns' (60% confidence) (UNUSED)

#### test_transform.py
- Line 788: unused function 'frame_mi' (60% confidence) (UNUSED)

#### conftest.py
- Line 13: unused function 'series_ints' (60% confidence) (UNUSED)
- Line 18: unused function 'frame_ints' (60% confidence) (UNUSED)
- Line 27: unused function 'series_uints' (60% confidence) (UNUSED)
- Line 35: unused function 'frame_uints' (60% confidence) (UNUSED)
- Line 44: unused function 'series_labels' (60% confidence) (UNUSED)
- Line 49: unused function 'frame_labels' (60% confidence) (UNUSED)
- Line 58: unused function 'series_ts' (60% confidence) (UNUSED)
- Line 66: unused function 'frame_ts' (60% confidence) (UNUSED)
- Line 74: unused function 'series_floats' (60% confidence) (UNUSED)
- Line 82: unused function 'frame_floats' (60% confidence) (UNUSED)
- Line 91: unused function 'series_mixed' (60% confidence) (UNUSED)
- Line 96: unused function 'frame_mixed' (60% confidence) (UNUSED)
- Line 103: unused function 'frame_empty' (60% confidence) (UNUSED)
- Line 108: unused function 'series_empty' (60% confidence) (UNUSED)
- Line 113: unused function 'frame_multi' (60% confidence) (UNUSED)
- Line 122: unused function 'series_multi' (60% confidence) (UNUSED)

#### test_coercion.py
- Line 28: unused function 'check_comprehensiveness' (60% confidence) (UNUSED)
- Line 263: unused variable 'insert_value' (100% confidence) (UNUSED)

#### test_odf.py
- Line 17: unused function 'cd_and_set_engine' (60% confidence) (UNUSED)

#### test_readers.py
- Line 160: unused method 'cd_and_set_engine' (60% confidence) (UNUSED)
- Line 1485: unused method 'cd_and_set_engine' (60% confidence) (UNUSED)

#### test_writers.py
- Line 68: unused function 'set_engine' (60% confidence) (UNUSED)

#### test_xlrd.py
- Line 20: unused function 'read_ext_xlrd' (60% confidence) (UNUSED)
- Line 30: unused variable 'read_ext_xlrd' (100% confidence) (UNUSED)

#### test_matplotlib.py
- Line 20: unused function 'mpl_cleanup' (60% confidence) (UNUSED)

#### test_eng_formatting.py
- Line 13: unused function 'reset_float_format' (60% confidence) (UNUSED)

#### test_to_excel.py
- Line 332: unused function 'tests_css_named_colors_valid' (60% confidence) (UNUSED)

#### test_json_table_schema.py
- Line 704: unused variable 'recwarn' (100% confidence) (UNUSED)
- Line 715: unused variable 'recwarn' (100% confidence) (UNUSED)
- Line 748: unused variable 'recwarn' (100% confidence) (UNUSED)
- Line 791: unused variable 'recwarn' (100% confidence) (UNUSED)
- Line 865: unused variable 'recwarn' (100% confidence) (UNUSED)

#### test_readlines.py
- Line 291: unused variable 'do_setlocale' (100% confidence) (UNUSED)

#### test_ujson.py
- Line 619: unused method 'toDict' (60% confidence) (UNUSED)
- Line 633: unused property 'recursive_attr' (60% confidence) (UNUSED)

#### conftest.py
- Line 56: unused method 'read_table_check_warnings' (60% confidence) (UNUSED)
- Line 285: unused function 'pyarrow_xfail' (60% confidence) (UNUSED)
- Line 304: unused function 'pyarrow_skip' (60% confidence) (UNUSED)

#### common.py
- Line 12: unused attribute 'MAX_NUMEXPR_THREADS' (60% confidence) (UNUSED)
- Line 13: unused attribute 'MAX_BLOSC_THREADS' (60% confidence) (UNUSED)
- Line 14: unused attribute 'MAX_THREADS' (60% confidence) (UNUSED)
- Line 17: unused function 'safe_close' (60% confidence) (UNUSED)

#### test_keys.py
- Line 47: unused variable 'value3' (60% confidence) (UNUSED)

#### test_xport.py
- Line 42: unused method 'test1_basic' (60% confidence) (UNUSED)
- Line 81: unused method 'test1_index' (60% confidence) (UNUSED)
- Line 103: unused method 'test1_incremental' (60% confidence) (UNUSED)
- Line 126: unused method 'test2_binary' (60% confidence) (UNUSED)

#### test_clipboard.py
- Line 101: unused function 'mock_ctypes' (60% confidence) (UNUSED)
- Line 176: unused function 'set_pyqt_clipboard' (60% confidence) (UNUSED)

#### test_sql.py
- Line 632: unused function 'mysql_pymysql_conn' (60% confidence) (UNUSED)
- Line 638: unused function 'mysql_pymysql_conn_iris' (60% confidence) (UNUSED)
- Line 644: unused function 'mysql_pymysql_conn_types' (60% confidence) (UNUSED)
- Line 679: unused function 'postgresql_psycopg2_conn' (60% confidence) (UNUSED)
- Line 700: unused function 'postgresql_adbc_iris' (60% confidence) (UNUSED)
- Line 719: unused function 'postgresql_adbc_types' (60% confidence) (UNUSED)
- Line 736: unused function 'postgresql_psycopg2_conn_iris' (60% confidence) (UNUSED)
- Line 742: unused function 'postgresql_psycopg2_conn_types' (60% confidence) (UNUSED)
- Line 773: unused function 'sqlite_str_iris' (60% confidence) (UNUSED)
- Line 796: unused function 'sqlite_str_types' (60% confidence) (UNUSED)
- Line 811: unused function 'sqlite_conn_types' (60% confidence) (UNUSED)
- Line 833: unused function 'sqlite_adbc_iris' (60% confidence) (UNUSED)
- Line 851: unused function 'sqlite_adbc_types' (60% confidence) (UNUSED)
- Line 887: unused function 'sqlite_buildin_types' (60% confidence) (UNUSED)
- Line 4052: unused variable 'not_null' (60% confidence) (UNUSED)

#### conftest.py
- Line 12: unused function 'mpl_cleanup' (60% confidence) (UNUSED)

#### test_backend.py
- Line 18: unused function 'restore_backend' (60% confidence) (UNUSED)
- Line 33: unused variable 'restore_backend' (100% confidence) (UNUSED)
- Line 43: unused variable 'restore_backend' (100% confidence) (UNUSED)
- Line 51: unused variable 'restore_backend' (100% confidence) (UNUSED)
- Line 93: unused variable 'restore_backend' (100% confidence) (UNUSED)

#### test_resample_api.py
- Line 191: unused function 'tests_raises_on_nuisance' (60% confidence) (UNUSED)
- Line 436: unused function 'b_sum' (60% confidence) (UNUSED)
- Line 441: unused function 'df_resample' (60% confidence) (UNUSED)
- Line 446: unused function 'df_col_resample' (60% confidence) (UNUSED)
- Line 451: unused function 'df_mult_resample' (60% confidence) (UNUSED)
- Line 456: unused function 'df_grouper_resample' (60% confidence) (UNUSED)

#### test_merge.py
- Line 1946: unused method 'tests_merge_categorical_unordered_equal' (60% confidence) (UNUSED)

#### test_algos.py
- Line 555: unused variable 'codes3' (60% confidence) (UNUSED)

#### test_expressions.py
- Line 68: unused function '_integer_integers' (60% confidence) (UNUSED)
- Line 74: unused function '_integer2' (60% confidence) (UNUSED)
- Line 88: unused function '_array2' (60% confidence) (UNUSED)
- Line 93: unused function '_array_mixed' (60% confidence) (UNUSED)
- Line 98: unused function '_array_mixed2' (60% confidence) (UNUSED)

#### test_nanops.py
- Line 21: unused function 'disable_bottleneck' (60% confidence) (UNUSED)
- Line 88: unused function 'arr_nan_nan' (60% confidence) (UNUSED)
- Line 98: unused function 'arr_float_inf' (60% confidence) (UNUSED)
- Line 103: unused function 'arr_nan_inf' (60% confidence) (UNUSED)
- Line 108: unused function 'arr_float_nan_inf' (60% confidence) (UNUSED)
- Line 113: unused function 'arr_nan_nan_inf' (60% confidence) (UNUSED)
- Line 118: unused function 'arr_obj' (60% confidence) (UNUSED)
- Line 142: unused function 'arr_complex_nan' (60% confidence) (UNUSED)
- Line 154: unused function 'arr_complex_nan_infj' (60% confidence) (UNUSED)
- Line 209: unused attribute 'arr_nan_nan' (60% confidence) (UNUSED)
- Line 212: unused attribute 'arr_float_inf' (60% confidence) (UNUSED)
- Line 214: unused attribute 'arr_nan_inf' (60% confidence) (UNUSED)
- Line 215: unused attribute 'arr_float_nan_inf' (60% confidence) (UNUSED)
- Line 216: unused attribute 'arr_nan_nan_inf' (60% confidence) (UNUSED)
- Line 217: unused attribute 'arr_obj' (60% confidence) (UNUSED)
- Line 232: unused attribute 'arr_complex_nan' (60% confidence) (UNUSED)
- Line 235: unused attribute 'arr_complex_nan_infj' (60% confidence) (UNUSED)
- Line 427: unused attribute 'arr_obj' (60% confidence) (UNUSED)
- Line 758: unused variable 'disable_bottleneck' (100% confidence) (UNUSED)
- Line 789: unused variable 'disable_bottleneck' (100% confidence) (UNUSED)
- Line 810: unused variable 'disable_bottleneck' (100% confidence) (UNUSED)
- Line 823: unused variable 'disable_bottleneck' (100% confidence) (UNUSED)
- Line 1240: unused variable 'disable_bottleneck' (100% confidence) (UNUSED)
- Line 1265: unused variable 'disable_bottleneck' (100% confidence) (UNUSED)

#### common.py
- Line 33: unused variable 'WED' (60% confidence) (UNUSED)

#### test_business_day.py
- Line 102: unused method 'testRollback1' (60% confidence) (UNUSED)
- Line 105: unused method 'testRollback2' (60% confidence) (UNUSED)
- Line 108: unused method 'testRollforward1' (60% confidence) (UNUSED)
- Line 111: unused method 'testRollforward2' (60% confidence) (UNUSED)

#### test_business_hour.py
- Line 250: unused method 'testRollback1' (60% confidence) (UNUSED)
- Line 290: unused method 'testRollback2' (60% confidence) (UNUSED)
- Line 295: unused method 'testRollforward1' (60% confidence) (UNUSED)
- Line 335: unused method 'testRollforward2' (60% confidence) (UNUSED)

#### test_custom_business_hour.py
- Line 107: unused method 'testRollback1' (60% confidence) (UNUSED)
- Line 119: unused method 'testRollback2' (60% confidence) (UNUSED)
- Line 124: unused method 'testRollforward1' (60% confidence) (UNUSED)
- Line 132: unused method 'testRollforward2' (60% confidence) (UNUSED)

#### test_custom_business_month.py
- Line 90: unused method 'testRollback1' (60% confidence) (UNUSED)
- Line 93: unused method 'testRollback2' (60% confidence) (UNUSED)
- Line 96: unused method 'testRollforward1' (60% confidence) (UNUSED)
- Line 280: unused method 'testRollback1' (60% confidence) (UNUSED)
- Line 283: unused method 'testRollback2' (60% confidence) (UNUSED)
- Line 286: unused method 'testRollforward1' (60% confidence) (UNUSED)

#### test_doc.py
- Line 7: unused variable 'whatever' (100% confidence) (UNUSED)
- Line 29: unused variable 'whatever' (100% confidence) (UNUSED)
- Line 34: unused variable 'whatever' (100% confidence) (UNUSED)
- Line 39: unused variable 'whatever' (100% confidence) (UNUSED)

#### test_api.py
- Line 59: unused function 'tests_skip_nuisance' (60% confidence) (UNUSED)

#### test_rolling.py
- Line 535: unused function 'tests_empty_df_rolling' (60% confidence) (UNUSED)

#### _decorators.py
- Line 337: unused attribute '__signature__' (60% confidence) (UNUSED)

#### __init__.py
- Line 107: unused variable 'VersionComparisonMethod' (60% confidence) (UNUSED)
- Line 243: unused property 'is_devrelease' (60% confidence) (UNUSED)
- Line 453: unused property 'is_devrelease' (60% confidence) (UNUSED)

#### packaging.py
- Line 217: unused class 'InstallWithGit' (60% confidence) (UNUSED)
- Line 231: unused class 'LocalInstall' (60% confidence) (UNUSED)
- Line 246: unused class 'TestrTest' (60% confidence) (UNUSED)
- Line 262: unused class 'LocalRPMVersion' (60% confidence) (UNUSED)
- Line 281: unused class 'LocalDebVersion' (60% confidence) (UNUSED)
- Line 307: unused class 'NoseTest' (60% confidence) (UNUSED)
- Line 446: unused class 'LocalDevelop' (60% confidence) (UNUSED)
- Line 458: unused class 'LocalInstallScripts' (60% confidence) (UNUSED)
- Line 558: unused class 'LocalEggInfo' (60% confidence) (UNUSED)
- Line 598: unused class 'LocalSDist' (60% confidence) (UNUSED)
- Line 662: unused variable 'LocalBuildDoc' (60% confidence) (UNUSED)
- Line 665: unused function 'have_sphinx' (60% confidence) (UNUSED)

#### __init__.py
- Line 19: unused function 'load_tests' (60% confidence) (UNUSED)

#### base.py
- Line 91: unused attribute 'log_fixture' (60% confidence) (UNUSED)

#### test_integration.py
- Line 31: unused variable 'PIPVERSION' (60% confidence) (UNUSED)

#### test_packaging.py
- Line 195: unused method '_setUp' (60% confidence) (UNUSED)
- Line 255: unused method '_setUp' (60% confidence) (UNUSED)
- Line 495: unused method 'testGitIsInstalled' (60% confidence) (UNUSED)
- Line 501: unused method 'testGitIsNotInstalled' (60% confidence) (UNUSED)

#### test_pbr_json.py
- Line 26: unused variable 'mock_get_git' (100% confidence) (UNUSED)
- Line 26: unused variable 'mock_get_is' (100% confidence) (UNUSED)
- Line 26: unused variable 'mock_run' (100% confidence) (UNUSED)

#### conf.py
- Line 29: unused variable 'source_suffix' (60% confidence) (UNUSED)
- Line 32: unused variable 'master_doc' (60% confidence) (UNUSED)
- Line 39: unused variable 'add_function_parentheses' (60% confidence) (UNUSED)
- Line 43: unused variable 'add_module_names' (60% confidence) (UNUSED)
- Line 54: unused variable 'latex_documents' (60% confidence) (UNUSED)

#### _setup_hooks.py
- Line 52: unused class 'test_command' (60% confidence) (UNUSED)

#### wsgi.py
- Line 36: unused class 'WSGI' (60% confidence) (UNUSED)

#### version.py
- Line 511: unused method 'cached_version_string' (60% confidence) (UNUSED)

#### _tkinter_finder.py
- Line 12: unused variable 'TKINTER_LIB' (60% confidence) (UNUSED)
- Line 14: unused variable 'TKINTER_LIB' (60% confidence) (UNUSED)
- Line 18: unused variable 'TKINTER_LIB' (60% confidence) (UNUSED)
- Line 20: unused variable 'tk_version' (60% confidence) (UNUSED)

#### AvifImagePlugin.py
- Line 23: unused function 'get_codec_version' (60% confidence) (UNUSED)
- Line 68: unused variable 'format_description' (60% confidence) (UNUSED)

#### BdfFontFile.py
- Line 92: unused class 'BdfFontFile' (60% confidence) (UNUSED)

#### BlpImagePlugin.py
- Line 51: unused variable 'UNCOMPRESSED_RAW_BGRA' (60% confidence) (UNUSED)
- Line 258: unused variable 'format_description' (60% confidence) (UNUSED)

#### BmpImagePlugin.py
- Line 69: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 403: unused variable 'format_description' (60% confidence) (UNUSED)

#### BufrStubImagePlugin.py
- Line 41: unused variable 'format_description' (60% confidence) (UNUSED)

#### CurImagePlugin.py
- Line 38: unused variable 'format_description' (60% confidence) (UNUSED)

#### DcxImagePlugin.py
- Line 43: unused variable 'format_description' (60% confidence) (UNUSED)

#### DdsImagePlugin.py
- Line 73: unused variable 'R32G32B32A32_TYPELESS' (60% confidence) (UNUSED)
- Line 74: unused variable 'R32G32B32A32_FLOAT' (60% confidence) (UNUSED)
- Line 75: unused variable 'R32G32B32A32_UINT' (60% confidence) (UNUSED)
- Line 76: unused variable 'R32G32B32A32_SINT' (60% confidence) (UNUSED)
- Line 77: unused variable 'R32G32B32_TYPELESS' (60% confidence) (UNUSED)
- Line 78: unused variable 'R32G32B32_FLOAT' (60% confidence) (UNUSED)
- Line 79: unused variable 'R32G32B32_UINT' (60% confidence) (UNUSED)
- Line 80: unused variable 'R32G32B32_SINT' (60% confidence) (UNUSED)
- Line 81: unused variable 'R16G16B16A16_TYPELESS' (60% confidence) (UNUSED)
- Line 82: unused variable 'R16G16B16A16_FLOAT' (60% confidence) (UNUSED)
- Line 83: unused variable 'R16G16B16A16_UNORM' (60% confidence) (UNUSED)
- Line 84: unused variable 'R16G16B16A16_UINT' (60% confidence) (UNUSED)
- Line 85: unused variable 'R16G16B16A16_SNORM' (60% confidence) (UNUSED)
- Line 86: unused variable 'R16G16B16A16_SINT' (60% confidence) (UNUSED)
- Line 87: unused variable 'R32G32_TYPELESS' (60% confidence) (UNUSED)
- Line 88: unused variable 'R32G32_FLOAT' (60% confidence) (UNUSED)
- Line 89: unused variable 'R32G32_UINT' (60% confidence) (UNUSED)
- Line 90: unused variable 'R32G32_SINT' (60% confidence) (UNUSED)
- Line 91: unused variable 'R32G8X24_TYPELESS' (60% confidence) (UNUSED)
- Line 92: unused variable 'D32_FLOAT_S8X24_UINT' (60% confidence) (UNUSED)
- Line 93: unused variable 'R32_FLOAT_X8X24_TYPELESS' (60% confidence) (UNUSED)
- Line 94: unused variable 'X32_TYPELESS_G8X24_UINT' (60% confidence) (UNUSED)
- Line 95: unused variable 'R10G10B10A2_TYPELESS' (60% confidence) (UNUSED)
- Line 96: unused variable 'R10G10B10A2_UNORM' (60% confidence) (UNUSED)
- Line 97: unused variable 'R10G10B10A2_UINT' (60% confidence) (UNUSED)
- Line 98: unused variable 'R11G11B10_FLOAT' (60% confidence) (UNUSED)
- Line 102: unused variable 'R8G8B8A8_UINT' (60% confidence) (UNUSED)
- Line 103: unused variable 'R8G8B8A8_SNORM' (60% confidence) (UNUSED)
- Line 104: unused variable 'R8G8B8A8_SINT' (60% confidence) (UNUSED)
- Line 105: unused variable 'R16G16_TYPELESS' (60% confidence) (UNUSED)
- Line 106: unused variable 'R16G16_FLOAT' (60% confidence) (UNUSED)
- Line 107: unused variable 'R16G16_UNORM' (60% confidence) (UNUSED)
- Line 108: unused variable 'R16G16_UINT' (60% confidence) (UNUSED)
- Line 109: unused variable 'R16G16_SNORM' (60% confidence) (UNUSED)
- Line 110: unused variable 'R16G16_SINT' (60% confidence) (UNUSED)
- Line 111: unused variable 'R32_TYPELESS' (60% confidence) (UNUSED)
- Line 112: unused variable 'D32_FLOAT' (60% confidence) (UNUSED)
- Line 113: unused variable 'R32_FLOAT' (60% confidence) (UNUSED)
- Line 114: unused variable 'R32_UINT' (60% confidence) (UNUSED)
- Line 115: unused variable 'R32_SINT' (60% confidence) (UNUSED)
- Line 116: unused variable 'R24G8_TYPELESS' (60% confidence) (UNUSED)
- Line 117: unused variable 'D24_UNORM_S8_UINT' (60% confidence) (UNUSED)
- Line 118: unused variable 'R24_UNORM_X8_TYPELESS' (60% confidence) (UNUSED)
- Line 119: unused variable 'X24_TYPELESS_G8_UINT' (60% confidence) (UNUSED)
- Line 120: unused variable 'R8G8_TYPELESS' (60% confidence) (UNUSED)
- Line 121: unused variable 'R8G8_UNORM' (60% confidence) (UNUSED)
- Line 122: unused variable 'R8G8_UINT' (60% confidence) (UNUSED)
- Line 123: unused variable 'R8G8_SNORM' (60% confidence) (UNUSED)
- Line 124: unused variable 'R8G8_SINT' (60% confidence) (UNUSED)
- Line 125: unused variable 'R16_TYPELESS' (60% confidence) (UNUSED)
- Line 126: unused variable 'R16_FLOAT' (60% confidence) (UNUSED)
- Line 127: unused variable 'D16_UNORM' (60% confidence) (UNUSED)
- Line 128: unused variable 'R16_UNORM' (60% confidence) (UNUSED)
- Line 129: unused variable 'R16_UINT' (60% confidence) (UNUSED)
- Line 130: unused variable 'R16_SNORM' (60% confidence) (UNUSED)
- Line 131: unused variable 'R16_SINT' (60% confidence) (UNUSED)
- Line 132: unused variable 'R8_TYPELESS' (60% confidence) (UNUSED)
- Line 133: unused variable 'R8_UNORM' (60% confidence) (UNUSED)
- Line 134: unused variable 'R8_UINT' (60% confidence) (UNUSED)
- Line 135: unused variable 'R8_SNORM' (60% confidence) (UNUSED)
- Line 136: unused variable 'R8_SINT' (60% confidence) (UNUSED)
- Line 137: unused variable 'A8_UNORM' (60% confidence) (UNUSED)
- Line 138: unused variable 'R1_UNORM' (60% confidence) (UNUSED)
- Line 139: unused variable 'R9G9B9E5_SHAREDEXP' (60% confidence) (UNUSED)
- Line 140: unused variable 'R8G8_B8G8_UNORM' (60% confidence) (UNUSED)
- Line 141: unused variable 'G8R8_G8B8_UNORM' (60% confidence) (UNUSED)
- Line 144: unused variable 'BC1_UNORM_SRGB' (60% confidence) (UNUSED)
- Line 147: unused variable 'BC2_UNORM_SRGB' (60% confidence) (UNUSED)
- Line 150: unused variable 'BC3_UNORM_SRGB' (60% confidence) (UNUSED)
- Line 153: unused variable 'BC4_SNORM' (60% confidence) (UNUSED)
- Line 157: unused variable 'B5G6R5_UNORM' (60% confidence) (UNUSED)
- Line 158: unused variable 'B5G5R5A1_UNORM' (60% confidence) (UNUSED)
- Line 159: unused variable 'B8G8R8A8_UNORM' (60% confidence) (UNUSED)
- Line 160: unused variable 'B8G8R8X8_UNORM' (60% confidence) (UNUSED)
- Line 161: unused variable 'R10G10B10_XR_BIAS_A2_UNORM' (60% confidence) (UNUSED)
- Line 162: unused variable 'B8G8R8A8_TYPELESS' (60% confidence) (UNUSED)
- Line 163: unused variable 'B8G8R8A8_UNORM_SRGB' (60% confidence) (UNUSED)
- Line 164: unused variable 'B8G8R8X8_TYPELESS' (60% confidence) (UNUSED)
- Line 165: unused variable 'B8G8R8X8_UNORM_SRGB' (60% confidence) (UNUSED)
- Line 166: unused variable 'BC6H_TYPELESS' (60% confidence) (UNUSED)
- Line 172: unused variable 'AYUV' (60% confidence) (UNUSED)
- Line 173: unused variable 'Y410' (60% confidence) (UNUSED)
- Line 174: unused variable 'Y416' (60% confidence) (UNUSED)
- Line 175: unused variable 'NV12' (60% confidence) (UNUSED)
- Line 176: unused variable 'P010' (60% confidence) (UNUSED)
- Line 177: unused variable 'P016' (60% confidence) (UNUSED)
- Line 178: unused variable 'OPAQUE_420' (60% confidence) (UNUSED)
- Line 179: unused variable 'YUY2' (60% confidence) (UNUSED)
- Line 180: unused variable 'Y210' (60% confidence) (UNUSED)
- Line 181: unused variable 'Y216' (60% confidence) (UNUSED)
- Line 182: unused variable 'NV11' (60% confidence) (UNUSED)
- Line 183: unused variable 'AI44' (60% confidence) (UNUSED)
- Line 184: unused variable 'IA44' (60% confidence) (UNUSED)
- Line 185: unused variable 'P8' (60% confidence) (UNUSED)
- Line 186: unused variable 'A8P8' (60% confidence) (UNUSED)
- Line 187: unused variable 'B4G4R4A4_UNORM' (60% confidence) (UNUSED)
- Line 188: unused variable 'P208' (60% confidence) (UNUSED)
- Line 189: unused variable 'V208' (60% confidence) (UNUSED)
- Line 190: unused variable 'V408' (60% confidence) (UNUSED)
- Line 191: unused variable 'SAMPLER_FEEDBACK_MIN_MIP_OPAQUE' (60% confidence) (UNUSED)
- Line 192: unused variable 'SAMPLER_FEEDBACK_MIP_REGION_USED_OPAQUE' (60% confidence) (UNUSED)
- Line 197: unused variable 'R8G8B8' (60% confidence) (UNUSED)
- Line 198: unused variable 'A8R8G8B8' (60% confidence) (UNUSED)
- Line 199: unused variable 'X8R8G8B8' (60% confidence) (UNUSED)
- Line 200: unused variable 'R5G6B5' (60% confidence) (UNUSED)
- Line 201: unused variable 'X1R5G5B5' (60% confidence) (UNUSED)
- Line 202: unused variable 'A1R5G5B5' (60% confidence) (UNUSED)
- Line 203: unused variable 'A4R4G4B4' (60% confidence) (UNUSED)
- Line 204: unused variable 'R3G3B2' (60% confidence) (UNUSED)
- Line 205: unused variable 'A8' (60% confidence) (UNUSED)
- Line 206: unused variable 'A8R3G3B2' (60% confidence) (UNUSED)
- Line 207: unused variable 'X4R4G4B4' (60% confidence) (UNUSED)
- Line 208: unused variable 'A2B10G10R10' (60% confidence) (UNUSED)
- Line 209: unused variable 'A8B8G8R8' (60% confidence) (UNUSED)
- Line 210: unused variable 'X8B8G8R8' (60% confidence) (UNUSED)
- Line 211: unused variable 'G16R16' (60% confidence) (UNUSED)
- Line 212: unused variable 'A2R10G10B10' (60% confidence) (UNUSED)
- Line 213: unused variable 'A16B16G16R16' (60% confidence) (UNUSED)
- Line 214: unused variable 'A8P8' (60% confidence) (UNUSED)
- Line 215: unused variable 'P8' (60% confidence) (UNUSED)
- Line 217: unused variable 'A8L8' (60% confidence) (UNUSED)
- Line 218: unused variable 'A4L4' (60% confidence) (UNUSED)
- Line 219: unused variable 'V8U8' (60% confidence) (UNUSED)
- Line 220: unused variable 'L6V5U5' (60% confidence) (UNUSED)
- Line 221: unused variable 'X8L8V8U8' (60% confidence) (UNUSED)
- Line 222: unused variable 'Q8W8V8U8' (60% confidence) (UNUSED)
- Line 223: unused variable 'V16U16' (60% confidence) (UNUSED)
- Line 224: unused variable 'A2W10V10U10' (60% confidence) (UNUSED)
- Line 225: unused variable 'D16_LOCKABLE' (60% confidence) (UNUSED)
- Line 226: unused variable 'D32' (60% confidence) (UNUSED)
- Line 227: unused variable 'D15S1' (60% confidence) (UNUSED)
- Line 228: unused variable 'D24S8' (60% confidence) (UNUSED)
- Line 229: unused variable 'D24X8' (60% confidence) (UNUSED)
- Line 230: unused variable 'D24X4S4' (60% confidence) (UNUSED)
- Line 231: unused variable 'D16' (60% confidence) (UNUSED)
- Line 232: unused variable 'D32F_LOCKABLE' (60% confidence) (UNUSED)
- Line 233: unused variable 'D24FS8' (60% confidence) (UNUSED)
- Line 234: unused variable 'D32_LOCKABLE' (60% confidence) (UNUSED)
- Line 235: unused variable 'S8_LOCKABLE' (60% confidence) (UNUSED)
- Line 236: unused variable 'L16' (60% confidence) (UNUSED)
- Line 237: unused variable 'VERTEXDATA' (60% confidence) (UNUSED)
- Line 238: unused variable 'INDEX16' (60% confidence) (UNUSED)
- Line 239: unused variable 'INDEX32' (60% confidence) (UNUSED)
- Line 240: unused variable 'Q16W16V16U16' (60% confidence) (UNUSED)
- Line 241: unused variable 'R16F' (60% confidence) (UNUSED)
- Line 242: unused variable 'G16R16F' (60% confidence) (UNUSED)
- Line 243: unused variable 'A16B16G16R16F' (60% confidence) (UNUSED)
- Line 244: unused variable 'R32F' (60% confidence) (UNUSED)
- Line 245: unused variable 'G32R32F' (60% confidence) (UNUSED)
- Line 246: unused variable 'A32B32G32R32F' (60% confidence) (UNUSED)
- Line 247: unused variable 'CxV8U8' (60% confidence) (UNUSED)
- Line 249: unused variable 'A2B10G10R10_XR_BIAS' (60% confidence) (UNUSED)
- Line 250: unused variable 'BINARYBUFFER' (60% confidence) (UNUSED)
- Line 252: unused variable 'UYVY' (60% confidence) (UNUSED)
- Line 253: unused variable 'R8G8_B8G8' (60% confidence) (UNUSED)
- Line 254: unused variable 'YUY2' (60% confidence) (UNUSED)
- Line 255: unused variable 'G8R8_G8B8' (60% confidence) (UNUSED)
- Line 257: unused variable 'DXT2' (60% confidence) (UNUSED)
- Line 259: unused variable 'DXT4' (60% confidence) (UNUSED)
- Line 262: unused variable 'BC4S' (60% confidence) (UNUSED)
- Line 268: unused variable 'MULTI2_ARGB8' (60% confidence) (UNUSED)
- Line 286: unused variable 'DDS_FOURCC' (60% confidence) (UNUSED)
- Line 287: unused variable 'DDS_RGB' (60% confidence) (UNUSED)
- Line 288: unused variable 'DDS_RGBA' (60% confidence) (UNUSED)
- Line 289: unused variable 'DDS_LUMINANCE' (60% confidence) (UNUSED)
- Line 290: unused variable 'DDS_LUMINANCEA' (60% confidence) (UNUSED)
- Line 291: unused variable 'DDS_ALPHA' (60% confidence) (UNUSED)
- Line 292: unused variable 'DDS_PAL8' (60% confidence) (UNUSED)
- Line 294: unused variable 'DDS_HEADER_FLAGS_TEXTURE' (60% confidence) (UNUSED)
- Line 295: unused variable 'DDS_HEADER_FLAGS_MIPMAP' (60% confidence) (UNUSED)
- Line 296: unused variable 'DDS_HEADER_FLAGS_VOLUME' (60% confidence) (UNUSED)
- Line 297: unused variable 'DDS_HEADER_FLAGS_PITCH' (60% confidence) (UNUSED)
- Line 298: unused variable 'DDS_HEADER_FLAGS_LINEARSIZE' (60% confidence) (UNUSED)
- Line 300: unused variable 'DDS_HEIGHT' (60% confidence) (UNUSED)
- Line 301: unused variable 'DDS_WIDTH' (60% confidence) (UNUSED)
- Line 303: unused variable 'DDS_SURFACE_FLAGS_TEXTURE' (60% confidence) (UNUSED)
- Line 304: unused variable 'DDS_SURFACE_FLAGS_MIPMAP' (60% confidence) (UNUSED)
- Line 305: unused variable 'DDS_SURFACE_FLAGS_CUBEMAP' (60% confidence) (UNUSED)
- Line 307: unused variable 'DDS_CUBEMAP_POSITIVEX' (60% confidence) (UNUSED)
- Line 308: unused variable 'DDS_CUBEMAP_NEGATIVEX' (60% confidence) (UNUSED)
- Line 309: unused variable 'DDS_CUBEMAP_POSITIVEY' (60% confidence) (UNUSED)
- Line 310: unused variable 'DDS_CUBEMAP_NEGATIVEY' (60% confidence) (UNUSED)
- Line 311: unused variable 'DDS_CUBEMAP_POSITIVEZ' (60% confidence) (UNUSED)
- Line 312: unused variable 'DDS_CUBEMAP_NEGATIVEZ' (60% confidence) (UNUSED)
- Line 314: unused variable 'DXT1_FOURCC' (60% confidence) (UNUSED)
- Line 315: unused variable 'DXT3_FOURCC' (60% confidence) (UNUSED)
- Line 316: unused variable 'DXT5_FOURCC' (60% confidence) (UNUSED)
- Line 318: unused variable 'DXGI_FORMAT_R8G8B8A8_TYPELESS' (60% confidence) (UNUSED)
- Line 319: unused variable 'DXGI_FORMAT_R8G8B8A8_UNORM' (60% confidence) (UNUSED)
- Line 320: unused variable 'DXGI_FORMAT_R8G8B8A8_UNORM_SRGB' (60% confidence) (UNUSED)
- Line 321: unused variable 'DXGI_FORMAT_BC5_TYPELESS' (60% confidence) (UNUSED)
- Line 322: unused variable 'DXGI_FORMAT_BC5_UNORM' (60% confidence) (UNUSED)
- Line 323: unused variable 'DXGI_FORMAT_BC5_SNORM' (60% confidence) (UNUSED)
- Line 324: unused variable 'DXGI_FORMAT_BC6H_UF16' (60% confidence) (UNUSED)
- Line 325: unused variable 'DXGI_FORMAT_BC6H_SF16' (60% confidence) (UNUSED)
- Line 326: unused variable 'DXGI_FORMAT_BC7_TYPELESS' (60% confidence) (UNUSED)
- Line 327: unused variable 'DXGI_FORMAT_BC7_UNORM' (60% confidence) (UNUSED)
- Line 328: unused variable 'DXGI_FORMAT_BC7_UNORM_SRGB' (60% confidence) (UNUSED)
- Line 333: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 353: unused variable 'mipmaps' (60% confidence) (UNUSED)
- Line 357: unused variable 'pfsize' (60% confidence) (UNUSED)

#### EpsImagePlugin.py
- Line 158: unused attribute 'dwFlags' (60% confidence) (UNUSED)
- Line 187: unused variable 'format_description' (60% confidence) (UNUSED)

#### ExifTags.py
- Line 23: unused variable 'InteropIndex' (60% confidence) (UNUSED)
- Line 24: unused variable 'ProcessingSoftware' (60% confidence) (UNUSED)
- Line 25: unused variable 'NewSubfileType' (60% confidence) (UNUSED)
- Line 26: unused variable 'SubfileType' (60% confidence) (UNUSED)
- Line 27: unused variable 'ImageWidth' (60% confidence) (UNUSED)
- Line 28: unused variable 'ImageLength' (60% confidence) (UNUSED)
- Line 29: unused variable 'BitsPerSample' (60% confidence) (UNUSED)
- Line 30: unused variable 'Compression' (60% confidence) (UNUSED)
- Line 31: unused variable 'PhotometricInterpretation' (60% confidence) (UNUSED)
- Line 32: unused variable 'Thresholding' (60% confidence) (UNUSED)
- Line 33: unused variable 'CellWidth' (60% confidence) (UNUSED)
- Line 34: unused variable 'CellLength' (60% confidence) (UNUSED)
- Line 35: unused variable 'FillOrder' (60% confidence) (UNUSED)
- Line 36: unused variable 'DocumentName' (60% confidence) (UNUSED)
- Line 37: unused variable 'ImageDescription' (60% confidence) (UNUSED)
- Line 38: unused variable 'Make' (60% confidence) (UNUSED)
- Line 40: unused variable 'StripOffsets' (60% confidence) (UNUSED)
- Line 42: unused variable 'SamplesPerPixel' (60% confidence) (UNUSED)
- Line 43: unused variable 'RowsPerStrip' (60% confidence) (UNUSED)
- Line 44: unused variable 'StripByteCounts' (60% confidence) (UNUSED)
- Line 45: unused variable 'MinSampleValue' (60% confidence) (UNUSED)
- Line 46: unused variable 'MaxSampleValue' (60% confidence) (UNUSED)
- Line 47: unused variable 'XResolution' (60% confidence) (UNUSED)
- Line 48: unused variable 'YResolution' (60% confidence) (UNUSED)
- Line 49: unused variable 'PlanarConfiguration' (60% confidence) (UNUSED)
- Line 51: unused variable 'FreeOffsets' (60% confidence) (UNUSED)
- Line 52: unused variable 'FreeByteCounts' (60% confidence) (UNUSED)
- Line 53: unused variable 'GrayResponseUnit' (60% confidence) (UNUSED)
- Line 54: unused variable 'GrayResponseCurve' (60% confidence) (UNUSED)
- Line 55: unused variable 'T4Options' (60% confidence) (UNUSED)
- Line 56: unused variable 'T6Options' (60% confidence) (UNUSED)
- Line 57: unused variable 'ResolutionUnit' (60% confidence) (UNUSED)
- Line 58: unused variable 'PageNumber' (60% confidence) (UNUSED)
- Line 59: unused variable 'TransferFunction' (60% confidence) (UNUSED)
- Line 60: unused variable 'Software' (60% confidence) (UNUSED)
- Line 63: unused variable 'HostComputer' (60% confidence) (UNUSED)
- Line 64: unused variable 'Predictor' (60% confidence) (UNUSED)
- Line 65: unused variable 'WhitePoint' (60% confidence) (UNUSED)
- Line 66: unused variable 'PrimaryChromaticities' (60% confidence) (UNUSED)
- Line 67: unused variable 'ColorMap' (60% confidence) (UNUSED)
- Line 68: unused variable 'HalftoneHints' (60% confidence) (UNUSED)
- Line 69: unused variable 'TileWidth' (60% confidence) (UNUSED)
- Line 70: unused variable 'TileLength' (60% confidence) (UNUSED)
- Line 71: unused variable 'TileOffsets' (60% confidence) (UNUSED)
- Line 72: unused variable 'TileByteCounts' (60% confidence) (UNUSED)
- Line 74: unused variable 'InkSet' (60% confidence) (UNUSED)
- Line 75: unused variable 'InkNames' (60% confidence) (UNUSED)
- Line 76: unused variable 'NumberOfInks' (60% confidence) (UNUSED)
- Line 77: unused variable 'DotRange' (60% confidence) (UNUSED)
- Line 78: unused variable 'TargetPrinter' (60% confidence) (UNUSED)
- Line 79: unused variable 'ExtraSamples' (60% confidence) (UNUSED)
- Line 80: unused variable 'SampleFormat' (60% confidence) (UNUSED)
- Line 81: unused variable 'SMinSampleValue' (60% confidence) (UNUSED)
- Line 82: unused variable 'SMaxSampleValue' (60% confidence) (UNUSED)
- Line 83: unused variable 'TransferRange' (60% confidence) (UNUSED)
- Line 84: unused variable 'ClipPath' (60% confidence) (UNUSED)
- Line 85: unused variable 'XClipPathUnits' (60% confidence) (UNUSED)
- Line 86: unused variable 'YClipPathUnits' (60% confidence) (UNUSED)
- Line 87: unused variable 'Indexed' (60% confidence) (UNUSED)
- Line 88: unused variable 'JPEGTables' (60% confidence) (UNUSED)
- Line 89: unused variable 'OPIProxy' (60% confidence) (UNUSED)
- Line 90: unused variable 'JPEGProc' (60% confidence) (UNUSED)
- Line 93: unused variable 'JpegRestartInterval' (60% confidence) (UNUSED)
- Line 94: unused variable 'JpegLosslessPredictors' (60% confidence) (UNUSED)
- Line 95: unused variable 'JpegPointTransforms' (60% confidence) (UNUSED)
- Line 96: unused variable 'JpegQTables' (60% confidence) (UNUSED)
- Line 97: unused variable 'JpegDCTables' (60% confidence) (UNUSED)
- Line 98: unused variable 'JpegACTables' (60% confidence) (UNUSED)
- Line 99: unused variable 'YCbCrCoefficients' (60% confidence) (UNUSED)
- Line 100: unused variable 'YCbCrSubSampling' (60% confidence) (UNUSED)
- Line 101: unused variable 'YCbCrPositioning' (60% confidence) (UNUSED)
- Line 102: unused variable 'ReferenceBlackWhite' (60% confidence) (UNUSED)
- Line 103: unused variable 'XMLPacket' (60% confidence) (UNUSED)
- Line 104: unused variable 'RelatedImageFileFormat' (60% confidence) (UNUSED)
- Line 105: unused variable 'RelatedImageWidth' (60% confidence) (UNUSED)
- Line 106: unused variable 'RelatedImageLength' (60% confidence) (UNUSED)
- Line 107: unused variable 'Rating' (60% confidence) (UNUSED)
- Line 108: unused variable 'RatingPercent' (60% confidence) (UNUSED)
- Line 109: unused variable 'ImageID' (60% confidence) (UNUSED)
- Line 110: unused variable 'CFARepeatPatternDim' (60% confidence) (UNUSED)
- Line 111: unused variable 'BatteryLevel' (60% confidence) (UNUSED)
- Line 112: unused variable 'Copyright' (60% confidence) (UNUSED)
- Line 113: unused variable 'ExposureTime' (60% confidence) (UNUSED)
- Line 114: unused variable 'FNumber' (60% confidence) (UNUSED)
- Line 115: unused variable 'IPTCNAA' (60% confidence) (UNUSED)
- Line 117: unused variable 'ExifOffset' (60% confidence) (UNUSED)
- Line 118: unused variable 'InterColorProfile' (60% confidence) (UNUSED)
- Line 119: unused variable 'ExposureProgram' (60% confidence) (UNUSED)
- Line 120: unused variable 'SpectralSensitivity' (60% confidence) (UNUSED)
- Line 122: unused variable 'ISOSpeedRatings' (60% confidence) (UNUSED)
- Line 123: unused variable 'OECF' (60% confidence) (UNUSED)
- Line 124: unused variable 'Interlace' (60% confidence) (UNUSED)
- Line 125: unused variable 'TimeZoneOffset' (60% confidence) (UNUSED)
- Line 126: unused variable 'SelfTimerMode' (60% confidence) (UNUSED)
- Line 127: unused variable 'SensitivityType' (60% confidence) (UNUSED)
- Line 128: unused variable 'StandardOutputSensitivity' (60% confidence) (UNUSED)
- Line 129: unused variable 'RecommendedExposureIndex' (60% confidence) (UNUSED)
- Line 130: unused variable 'ISOSpeed' (60% confidence) (UNUSED)
- Line 131: unused variable 'ISOSpeedLatitudeyyy' (60% confidence) (UNUSED)
- Line 132: unused variable 'ISOSpeedLatitudezzz' (60% confidence) (UNUSED)
- Line 133: unused variable 'ExifVersion' (60% confidence) (UNUSED)
- Line 134: unused variable 'DateTimeOriginal' (60% confidence) (UNUSED)
- Line 135: unused variable 'DateTimeDigitized' (60% confidence) (UNUSED)
- Line 136: unused variable 'OffsetTime' (60% confidence) (UNUSED)
- Line 137: unused variable 'OffsetTimeOriginal' (60% confidence) (UNUSED)
- Line 138: unused variable 'OffsetTimeDigitized' (60% confidence) (UNUSED)
- Line 139: unused variable 'ComponentsConfiguration' (60% confidence) (UNUSED)
- Line 140: unused variable 'CompressedBitsPerPixel' (60% confidence) (UNUSED)
- Line 141: unused variable 'ShutterSpeedValue' (60% confidence) (UNUSED)
- Line 142: unused variable 'ApertureValue' (60% confidence) (UNUSED)
- Line 143: unused variable 'BrightnessValue' (60% confidence) (UNUSED)
- Line 144: unused variable 'ExposureBiasValue' (60% confidence) (UNUSED)
- Line 145: unused variable 'MaxApertureValue' (60% confidence) (UNUSED)
- Line 146: unused variable 'SubjectDistance' (60% confidence) (UNUSED)
- Line 147: unused variable 'MeteringMode' (60% confidence) (UNUSED)
- Line 148: unused variable 'LightSource' (60% confidence) (UNUSED)
- Line 149: unused variable 'Flash' (60% confidence) (UNUSED)
- Line 150: unused variable 'FocalLength' (60% confidence) (UNUSED)
- Line 151: unused variable 'Noise' (60% confidence) (UNUSED)
- Line 152: unused variable 'ImageNumber' (60% confidence) (UNUSED)
- Line 153: unused variable 'SecurityClassification' (60% confidence) (UNUSED)
- Line 154: unused variable 'ImageHistory' (60% confidence) (UNUSED)
- Line 155: unused variable 'TIFFEPStandardID' (60% confidence) (UNUSED)
- Line 157: unused variable 'UserComment' (60% confidence) (UNUSED)
- Line 158: unused variable 'SubsecTime' (60% confidence) (UNUSED)
- Line 159: unused variable 'SubsecTimeOriginal' (60% confidence) (UNUSED)
- Line 160: unused variable 'SubsecTimeDigitized' (60% confidence) (UNUSED)
- Line 161: unused variable 'AmbientTemperature' (60% confidence) (UNUSED)
- Line 162: unused variable 'Humidity' (60% confidence) (UNUSED)
- Line 163: unused variable 'Pressure' (60% confidence) (UNUSED)
- Line 164: unused variable 'WaterDepth' (60% confidence) (UNUSED)
- Line 165: unused variable 'Acceleration' (60% confidence) (UNUSED)
- Line 166: unused variable 'CameraElevationAngle' (60% confidence) (UNUSED)
- Line 167: unused variable 'XPTitle' (60% confidence) (UNUSED)
- Line 168: unused variable 'XPComment' (60% confidence) (UNUSED)
- Line 169: unused variable 'XPAuthor' (60% confidence) (UNUSED)
- Line 170: unused variable 'XPKeywords' (60% confidence) (UNUSED)
- Line 171: unused variable 'XPSubject' (60% confidence) (UNUSED)
- Line 172: unused variable 'FlashPixVersion' (60% confidence) (UNUSED)
- Line 173: unused variable 'ColorSpace' (60% confidence) (UNUSED)
- Line 174: unused variable 'ExifImageWidth' (60% confidence) (UNUSED)
- Line 175: unused variable 'ExifImageHeight' (60% confidence) (UNUSED)
- Line 176: unused variable 'RelatedSoundFile' (60% confidence) (UNUSED)
- Line 177: unused variable 'ExifInteroperabilityOffset' (60% confidence) (UNUSED)
- Line 178: unused variable 'FlashEnergy' (60% confidence) (UNUSED)
- Line 179: unused variable 'SpatialFrequencyResponse' (60% confidence) (UNUSED)
- Line 180: unused variable 'FocalPlaneXResolution' (60% confidence) (UNUSED)
- Line 181: unused variable 'FocalPlaneYResolution' (60% confidence) (UNUSED)
- Line 182: unused variable 'FocalPlaneResolutionUnit' (60% confidence) (UNUSED)
- Line 183: unused variable 'SubjectLocation' (60% confidence) (UNUSED)
- Line 184: unused variable 'ExposureIndex' (60% confidence) (UNUSED)
- Line 185: unused variable 'SensingMethod' (60% confidence) (UNUSED)
- Line 186: unused variable 'FileSource' (60% confidence) (UNUSED)
- Line 187: unused variable 'SceneType' (60% confidence) (UNUSED)
- Line 188: unused variable 'CFAPattern' (60% confidence) (UNUSED)
- Line 189: unused variable 'CustomRendered' (60% confidence) (UNUSED)
- Line 190: unused variable 'ExposureMode' (60% confidence) (UNUSED)
- Line 191: unused variable 'WhiteBalance' (60% confidence) (UNUSED)
- Line 192: unused variable 'DigitalZoomRatio' (60% confidence) (UNUSED)
- Line 193: unused variable 'FocalLengthIn35mmFilm' (60% confidence) (UNUSED)
- Line 194: unused variable 'SceneCaptureType' (60% confidence) (UNUSED)
- Line 195: unused variable 'GainControl' (60% confidence) (UNUSED)
- Line 196: unused variable 'Contrast' (60% confidence) (UNUSED)
- Line 197: unused variable 'Saturation' (60% confidence) (UNUSED)
- Line 198: unused variable 'Sharpness' (60% confidence) (UNUSED)
- Line 199: unused variable 'DeviceSettingDescription' (60% confidence) (UNUSED)
- Line 200: unused variable 'SubjectDistanceRange' (60% confidence) (UNUSED)
- Line 201: unused variable 'ImageUniqueID' (60% confidence) (UNUSED)
- Line 202: unused variable 'CameraOwnerName' (60% confidence) (UNUSED)
- Line 203: unused variable 'BodySerialNumber' (60% confidence) (UNUSED)
- Line 204: unused variable 'LensSpecification' (60% confidence) (UNUSED)
- Line 205: unused variable 'LensMake' (60% confidence) (UNUSED)
- Line 206: unused variable 'LensModel' (60% confidence) (UNUSED)
- Line 207: unused variable 'LensSerialNumber' (60% confidence) (UNUSED)
- Line 208: unused variable 'CompositeImage' (60% confidence) (UNUSED)
- Line 209: unused variable 'CompositeImageCount' (60% confidence) (UNUSED)
- Line 210: unused variable 'CompositeImageExposureTimes' (60% confidence) (UNUSED)
- Line 211: unused variable 'Gamma' (60% confidence) (UNUSED)
- Line 212: unused variable 'PrintImageMatching' (60% confidence) (UNUSED)
- Line 213: unused variable 'DNGVersion' (60% confidence) (UNUSED)
- Line 214: unused variable 'DNGBackwardVersion' (60% confidence) (UNUSED)
- Line 215: unused variable 'UniqueCameraModel' (60% confidence) (UNUSED)
- Line 216: unused variable 'LocalizedCameraModel' (60% confidence) (UNUSED)
- Line 217: unused variable 'CFAPlaneColor' (60% confidence) (UNUSED)
- Line 218: unused variable 'CFALayout' (60% confidence) (UNUSED)
- Line 219: unused variable 'LinearizationTable' (60% confidence) (UNUSED)
- Line 220: unused variable 'BlackLevelRepeatDim' (60% confidence) (UNUSED)
- Line 221: unused variable 'BlackLevel' (60% confidence) (UNUSED)
- Line 222: unused variable 'BlackLevelDeltaH' (60% confidence) (UNUSED)
- Line 223: unused variable 'BlackLevelDeltaV' (60% confidence) (UNUSED)
- Line 224: unused variable 'WhiteLevel' (60% confidence) (UNUSED)
- Line 225: unused variable 'DefaultScale' (60% confidence) (UNUSED)
- Line 226: unused variable 'DefaultCropOrigin' (60% confidence) (UNUSED)
- Line 227: unused variable 'DefaultCropSize' (60% confidence) (UNUSED)
- Line 228: unused variable 'ColorMatrix1' (60% confidence) (UNUSED)
- Line 229: unused variable 'ColorMatrix2' (60% confidence) (UNUSED)
- Line 230: unused variable 'CameraCalibration1' (60% confidence) (UNUSED)
- Line 231: unused variable 'CameraCalibration2' (60% confidence) (UNUSED)
- Line 232: unused variable 'ReductionMatrix1' (60% confidence) (UNUSED)
- Line 233: unused variable 'ReductionMatrix2' (60% confidence) (UNUSED)
- Line 234: unused variable 'AnalogBalance' (60% confidence) (UNUSED)
- Line 235: unused variable 'AsShotNeutral' (60% confidence) (UNUSED)
- Line 236: unused variable 'AsShotWhiteXY' (60% confidence) (UNUSED)
- Line 237: unused variable 'BaselineExposure' (60% confidence) (UNUSED)
- Line 238: unused variable 'BaselineNoise' (60% confidence) (UNUSED)
- Line 239: unused variable 'BaselineSharpness' (60% confidence) (UNUSED)
- Line 240: unused variable 'BayerGreenSplit' (60% confidence) (UNUSED)
- Line 241: unused variable 'LinearResponseLimit' (60% confidence) (UNUSED)
- Line 242: unused variable 'CameraSerialNumber' (60% confidence) (UNUSED)
- Line 243: unused variable 'LensInfo' (60% confidence) (UNUSED)
- Line 244: unused variable 'ChromaBlurRadius' (60% confidence) (UNUSED)
- Line 245: unused variable 'AntiAliasStrength' (60% confidence) (UNUSED)
- Line 246: unused variable 'ShadowScale' (60% confidence) (UNUSED)
- Line 247: unused variable 'DNGPrivateData' (60% confidence) (UNUSED)
- Line 248: unused variable 'MakerNoteSafety' (60% confidence) (UNUSED)
- Line 249: unused variable 'CalibrationIlluminant1' (60% confidence) (UNUSED)
- Line 250: unused variable 'CalibrationIlluminant2' (60% confidence) (UNUSED)
- Line 251: unused variable 'BestQualityScale' (60% confidence) (UNUSED)
- Line 252: unused variable 'RawDataUniqueID' (60% confidence) (UNUSED)
- Line 253: unused variable 'OriginalRawFileName' (60% confidence) (UNUSED)
- Line 254: unused variable 'OriginalRawFileData' (60% confidence) (UNUSED)
- Line 255: unused variable 'ActiveArea' (60% confidence) (UNUSED)
- Line 256: unused variable 'MaskedAreas' (60% confidence) (UNUSED)
- Line 257: unused variable 'AsShotICCProfile' (60% confidence) (UNUSED)
- Line 258: unused variable 'AsShotPreProfileMatrix' (60% confidence) (UNUSED)
- Line 259: unused variable 'CurrentICCProfile' (60% confidence) (UNUSED)
- Line 260: unused variable 'CurrentPreProfileMatrix' (60% confidence) (UNUSED)
- Line 261: unused variable 'ColorimetricReference' (60% confidence) (UNUSED)
- Line 262: unused variable 'CameraCalibrationSignature' (60% confidence) (UNUSED)
- Line 263: unused variable 'ProfileCalibrationSignature' (60% confidence) (UNUSED)
- Line 264: unused variable 'AsShotProfileName' (60% confidence) (UNUSED)
- Line 265: unused variable 'NoiseReductionApplied' (60% confidence) (UNUSED)
- Line 266: unused variable 'ProfileName' (60% confidence) (UNUSED)
- Line 267: unused variable 'ProfileHueSatMapDims' (60% confidence) (UNUSED)
- Line 268: unused variable 'ProfileHueSatMapData1' (60% confidence) (UNUSED)
- Line 269: unused variable 'ProfileHueSatMapData2' (60% confidence) (UNUSED)
- Line 270: unused variable 'ProfileToneCurve' (60% confidence) (UNUSED)
- Line 271: unused variable 'ProfileEmbedPolicy' (60% confidence) (UNUSED)
- Line 272: unused variable 'ProfileCopyright' (60% confidence) (UNUSED)
- Line 273: unused variable 'ForwardMatrix1' (60% confidence) (UNUSED)
- Line 274: unused variable 'ForwardMatrix2' (60% confidence) (UNUSED)
- Line 275: unused variable 'PreviewApplicationName' (60% confidence) (UNUSED)
- Line 276: unused variable 'PreviewApplicationVersion' (60% confidence) (UNUSED)
- Line 277: unused variable 'PreviewSettingsName' (60% confidence) (UNUSED)
- Line 278: unused variable 'PreviewSettingsDigest' (60% confidence) (UNUSED)
- Line 279: unused variable 'PreviewColorSpace' (60% confidence) (UNUSED)
- Line 280: unused variable 'PreviewDateTime' (60% confidence) (UNUSED)
- Line 281: unused variable 'RawImageDigest' (60% confidence) (UNUSED)
- Line 282: unused variable 'OriginalRawFileDigest' (60% confidence) (UNUSED)
- Line 283: unused variable 'SubTileBlockSize' (60% confidence) (UNUSED)
- Line 284: unused variable 'RowInterleaveFactor' (60% confidence) (UNUSED)
- Line 285: unused variable 'ProfileLookTableDims' (60% confidence) (UNUSED)
- Line 286: unused variable 'ProfileLookTableData' (60% confidence) (UNUSED)
- Line 287: unused variable 'OpcodeList1' (60% confidence) (UNUSED)
- Line 288: unused variable 'OpcodeList2' (60% confidence) (UNUSED)
- Line 289: unused variable 'OpcodeList3' (60% confidence) (UNUSED)
- Line 290: unused variable 'NoiseProfile' (60% confidence) (UNUSED)
- Line 306: unused variable 'GPSVersionID' (60% confidence) (UNUSED)
- Line 307: unused variable 'GPSLatitudeRef' (60% confidence) (UNUSED)
- Line 308: unused variable 'GPSLatitude' (60% confidence) (UNUSED)
- Line 309: unused variable 'GPSLongitudeRef' (60% confidence) (UNUSED)
- Line 310: unused variable 'GPSLongitude' (60% confidence) (UNUSED)
- Line 311: unused variable 'GPSAltitudeRef' (60% confidence) (UNUSED)
- Line 312: unused variable 'GPSAltitude' (60% confidence) (UNUSED)
- Line 313: unused variable 'GPSTimeStamp' (60% confidence) (UNUSED)
- Line 314: unused variable 'GPSSatellites' (60% confidence) (UNUSED)
- Line 315: unused variable 'GPSStatus' (60% confidence) (UNUSED)
- Line 316: unused variable 'GPSMeasureMode' (60% confidence) (UNUSED)
- Line 317: unused variable 'GPSDOP' (60% confidence) (UNUSED)
- Line 318: unused variable 'GPSSpeedRef' (60% confidence) (UNUSED)
- Line 319: unused variable 'GPSSpeed' (60% confidence) (UNUSED)
- Line 320: unused variable 'GPSTrackRef' (60% confidence) (UNUSED)
- Line 321: unused variable 'GPSTrack' (60% confidence) (UNUSED)
- Line 322: unused variable 'GPSImgDirectionRef' (60% confidence) (UNUSED)
- Line 323: unused variable 'GPSImgDirection' (60% confidence) (UNUSED)
- Line 324: unused variable 'GPSMapDatum' (60% confidence) (UNUSED)
- Line 325: unused variable 'GPSDestLatitudeRef' (60% confidence) (UNUSED)
- Line 326: unused variable 'GPSDestLatitude' (60% confidence) (UNUSED)
- Line 327: unused variable 'GPSDestLongitudeRef' (60% confidence) (UNUSED)
- Line 328: unused variable 'GPSDestLongitude' (60% confidence) (UNUSED)
- Line 329: unused variable 'GPSDestBearingRef' (60% confidence) (UNUSED)
- Line 330: unused variable 'GPSDestBearing' (60% confidence) (UNUSED)
- Line 331: unused variable 'GPSDestDistanceRef' (60% confidence) (UNUSED)
- Line 332: unused variable 'GPSDestDistance' (60% confidence) (UNUSED)
- Line 333: unused variable 'GPSProcessingMethod' (60% confidence) (UNUSED)
- Line 334: unused variable 'GPSAreaInformation' (60% confidence) (UNUSED)
- Line 335: unused variable 'GPSDateStamp' (60% confidence) (UNUSED)
- Line 336: unused variable 'GPSDifferential' (60% confidence) (UNUSED)
- Line 337: unused variable 'GPSHPositioningError' (60% confidence) (UNUSED)
- Line 341: unused variable 'GPSTAGS' (60% confidence) (UNUSED)
- Line 345: unused variable 'InteropIndex' (60% confidence) (UNUSED)
- Line 346: unused variable 'InteropVersion' (60% confidence) (UNUSED)
- Line 347: unused variable 'RelatedImageFileFormat' (60% confidence) (UNUSED)
- Line 348: unused variable 'RelatedImageWidth' (60% confidence) (UNUSED)
- Line 349: unused variable 'RelatedImageHeight' (60% confidence) (UNUSED)
- Line 356: unused variable 'Makernote' (60% confidence) (UNUSED)
- Line 361: unused class 'LightSource' (60% confidence) (UNUSED)
- Line 363: unused variable 'Daylight' (60% confidence) (UNUSED)
- Line 364: unused variable 'Fluorescent' (60% confidence) (UNUSED)
- Line 365: unused variable 'Tungsten' (60% confidence) (UNUSED)
- Line 366: unused variable 'Flash' (60% confidence) (UNUSED)
- Line 367: unused variable 'Fine' (60% confidence) (UNUSED)
- Line 368: unused variable 'Cloudy' (60% confidence) (UNUSED)
- Line 369: unused variable 'Shade' (60% confidence) (UNUSED)
- Line 370: unused variable 'DaylightFluorescent' (60% confidence) (UNUSED)
- Line 371: unused variable 'DayWhiteFluorescent' (60% confidence) (UNUSED)
- Line 372: unused variable 'CoolWhiteFluorescent' (60% confidence) (UNUSED)
- Line 373: unused variable 'WhiteFluorescent' (60% confidence) (UNUSED)
- Line 374: unused variable 'StandardLightA' (60% confidence) (UNUSED)
- Line 375: unused variable 'StandardLightB' (60% confidence) (UNUSED)
- Line 376: unused variable 'StandardLightC' (60% confidence) (UNUSED)
- Line 377: unused variable 'D55' (60% confidence) (UNUSED)
- Line 378: unused variable 'D65' (60% confidence) (UNUSED)
- Line 379: unused variable 'D75' (60% confidence) (UNUSED)
- Line 380: unused variable 'D50' (60% confidence) (UNUSED)
- Line 381: unused variable 'ISO' (60% confidence) (UNUSED)

#### FitsImagePlugin.py
- Line 25: unused variable 'format_description' (60% confidence) (UNUSED)

#### FliImagePlugin.py
- Line 46: unused variable 'format_description' (60% confidence) (UNUSED)

#### FpxImagePlugin.py
- Line 54: unused variable 'format_description' (60% confidence) (UNUSED)

#### FtexImagePlugin.py
- Line 72: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 80: unused variable 'mipmap_count' (60% confidence) (UNUSED)

#### GbrImagePlugin.py
- Line 42: unused variable 'format_description' (60% confidence) (UNUSED)

#### GdImageFile.py
- Line 47: unused variable 'format_description' (60% confidence) (UNUSED)

#### GifImagePlugin.py
- Line 82: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 866: unused function '_save_netpbm' (60% confidence) (UNUSED)

#### GribStubImagePlugin.py
- Line 41: unused variable 'format_description' (60% confidence) (UNUSED)

#### Hdf5StubImagePlugin.py
- Line 41: unused variable 'format_description' (60% confidence) (UNUSED)

#### IcnsImagePlugin.py
- Line 266: unused variable 'format_description' (60% confidence) (UNUSED)

#### IcoImagePlugin.py
- Line 326: unused variable 'format_description' (60% confidence) (UNUSED)

#### Image.py
- Line 118: unused function 'isImageType' (60% confidence) (UNUSED)
- Line 179: unused variable 'ORDERED' (60% confidence) (UNUSED)
- Line 180: unused variable 'RASTERIZE' (60% confidence) (UNUSED)
- Line 192: unused variable 'MAXCOVERAGE' (60% confidence) (UNUSED)
- Line 306: unused function 'getmodebandnames' (60% confidence) (UNUSED)
- Line 540: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 689: unused method '_repr_pretty_' (60% confidence) (UNUSED)
- Line 712: unused method '_repr_png_' (60% confidence) (UNUSED)
- Line 719: unused method '_repr_jpeg_' (60% confidence) (UNUSED)
- Line 1474: unused method 'getxmp' (60% confidence) (UNUSED)
- Line 3329: unused function 'fromarrow' (60% confidence) (UNUSED)
- Line 3769: unused function 'registered_extensions' (60% confidence) (UNUSED)
- Line 4193: unused method 'hide_offsets' (60% confidence) (UNUSED)

#### ImageChops.py
- Line 54: unused function 'lighter' (60% confidence) (UNUSED)
- Line 69: unused function 'darker' (60% confidence) (UNUSED)
- Line 130: unused function 'soft_light' (60% confidence) (UNUSED)
- Line 142: unused function 'hard_light' (60% confidence) (UNUSED)
- Line 200: unused function 'add_modulo' (60% confidence) (UNUSED)

#### ImageCms.py
- Line 134: unused variable 'RELATIVE_COLORIMETRIC' (60% confidence) (UNUSED)
- Line 135: unused variable 'SATURATION' (60% confidence) (UNUSED)
- Line 140: unused variable 'INPUT' (60% confidence) (UNUSED)
- Line 141: unused variable 'OUTPUT' (60% confidence) (UNUSED)
- Line 142: unused variable 'PROOF' (60% confidence) (UNUSED)
- Line 153: unused variable 'NOCACHE' (60% confidence) (UNUSED)
- Line 155: unused variable 'NOOPTIMIZE' (60% confidence) (UNUSED)
- Line 157: unused variable 'NULLTRANSFORM' (60% confidence) (UNUSED)
- Line 159: unused variable 'GAMUTCHECK' (60% confidence) (UNUSED)
- Line 163: unused variable 'BLACKPOINTCOMPENSATION' (60% confidence) (UNUSED)
- Line 164: unused variable 'NOWHITEONWHITEFIXUP' (60% confidence) (UNUSED)
- Line 166: unused variable 'HIGHRESPRECALC' (60% confidence) (UNUSED)
- Line 168: unused variable 'LOWRESPRECALC' (60% confidence) (UNUSED)
- Line 171: unused variable 'USE_8BITS_DEVICELINK' (60% confidence) (UNUSED)
- Line 173: unused variable 'GUESSDEVICECLASS' (60% confidence) (UNUSED)
- Line 175: unused variable 'KEEP_SEQUENCE' (60% confidence) (UNUSED)
- Line 177: unused variable 'FORCE_CLUT' (60% confidence) (UNUSED)
- Line 179: unused variable 'CLUT_POST_LINEARIZATION' (60% confidence) (UNUSED)
- Line 181: unused variable 'CLUT_PRE_LINEARIZATION' (60% confidence) (UNUSED)
- Line 183: unused variable 'NONEGATIVES' (60% confidence) (UNUSED)
- Line 185: unused variable 'COPY_ALPHA' (60% confidence) (UNUSED)
- Line 187: unused variable 'NODEFAULTRESOURCEDEF' (60% confidence) (UNUSED)
- Line 198: unused method 'GRIDPOINTS' (60% confidence) (UNUSED)
- Line 273: unused attribute 'product_name' (60% confidence) (UNUSED)
- Line 274: unused attribute 'product_info' (60% confidence) (UNUSED)
- Line 347: unused attribute 'inputMode' (60% confidence) (UNUSED)
- Line 371: unused function 'get_display_profile' (60% confidence) (UNUSED)
- Line 404: unused function 'profileToProfile' (60% confidence) (UNUSED)
- Line 500: unused function 'getOpenProfile' (60% confidence) (UNUSED)
- Line 720: unused variable 'buildTransformFromOpenProfiles' (60% confidence) (UNUSED)
- Line 721: unused variable 'buildProofTransformFromOpenProfiles' (60% confidence) (UNUSED)
- Line 724: unused function 'applyTransform' (60% confidence) (UNUSED)
- Line 830: unused function 'getProfileName' (60% confidence) (UNUSED)
- Line 872: unused function 'getProfileInfo' (60% confidence) (UNUSED)
- Line 909: unused function 'getProfileCopyright' (60% confidence) (UNUSED)
- Line 937: unused function 'getProfileManufacturer' (60% confidence) (UNUSED)
- Line 965: unused function 'getProfileModel' (60% confidence) (UNUSED)
- Line 994: unused function 'getProfileDescription' (60% confidence) (UNUSED)
- Line 1023: unused function 'getDefaultIntent' (60% confidence) (UNUSED)
- Line 1062: unused function 'isIntentSupported' (60% confidence) (UNUSED)

#### ImageDraw.py
- Line 45: unused variable 'Outline' (60% confidence) (UNUSED)
- Line 194: unused method 'chord' (60% confidence) (UNUSED)
- Line 385: unused method 'regular_polygon' (60% confidence) (UNUSED)
- Line 412: unused method 'rounded_rectangle' (60% confidence) (UNUSED)
- Line 1027: unused function 'floodfill' (60% confidence) (UNUSED)

#### ImageDraw2.py
- Line 118: unused method 'settransform' (60% confidence) (UNUSED)
- Line 139: unused method 'chord' (60% confidence) (UNUSED)

#### ImageEnhance.py
- Line 29: unused method 'enhance' (60% confidence) (UNUSED)
- Line 63: unused class 'Contrast' (60% confidence) (UNUSED)
- Line 84: unused class 'Brightness' (60% confidence) (UNUSED)
- Line 100: unused class 'Sharpness' (60% confidence) (UNUSED)

#### ImageFile.py
- Line 86: unused function 'raise_oserror' (60% confidence) (UNUSED)
- Line 248: unused method 'get_format_mimetype' (60% confidence) (UNUSED)

#### ImageFilter.py
- Line 110: unused class 'MedianFilter' (60% confidence) (UNUSED)
- Line 125: unused class 'MinFilter' (60% confidence) (UNUSED)
- Line 140: unused class 'MaxFilter' (60% confidence) (UNUSED)
- Line 155: unused class 'ModeFilter' (60% confidence) (UNUSED)
- Line 173: unused class 'GaussianBlur' (60% confidence) (UNUSED)
- Line 196: unused class 'BoxBlur' (60% confidence) (UNUSED)
- Line 228: unused class 'UnsharpMask' (60% confidence) (UNUSED)
- Line 256: unused class 'BLUR' (60% confidence) (UNUSED)
- Line 269: unused class 'CONTOUR' (60% confidence) (UNUSED)
- Line 280: unused class 'DETAIL' (60% confidence) (UNUSED)
- Line 291: unused class 'EDGE_ENHANCE' (60% confidence) (UNUSED)
- Line 302: unused class 'EDGE_ENHANCE_MORE' (60% confidence) (UNUSED)
- Line 313: unused class 'EMBOSS' (60% confidence) (UNUSED)
- Line 324: unused class 'FIND_EDGES' (60% confidence) (UNUSED)
- Line 335: unused class 'SHARPEN' (60% confidence) (UNUSED)
- Line 357: unused class 'SMOOTH_MORE' (60% confidence) (UNUSED)

#### ImageFont.py
- Line 305: unused method 'getmetrics' (60% confidence) (UNUSED)
- Line 654: unused method 'font_variant' (60% confidence) (UNUSED)
- Line 715: unused method 'get_variation_axes' (60% confidence) (UNUSED)
- Line 730: unused method 'set_variation_by_axes' (60% confidence) (UNUSED)
- Line 920: unused variable 'walkdir' (60% confidence) (UNUSED)
- Line 935: unused function 'load_path' (60% confidence) (UNUSED)

#### ImageGrab.py
- Line 116: unused function 'grabclipboard' (60% confidence) (UNUSED)

#### ImageMorph.py
- Line 92: unused method 'add_patterns' (60% confidence) (UNUSED)
- Line 100: unused method 'get_lut' (60% confidence) (UNUSED)
- Line 187: unused class 'MorphOp' (60% confidence) (UNUSED)
- Line 245: unused method 'load_lut' (60% confidence) (UNUSED)
- Line 255: unused method 'save_lut' (60% confidence) (UNUSED)
- Line 263: unused method 'set_lut' (60% confidence) (UNUSED)

#### ImageOps.py
- Line 70: unused function 'autocontrast' (60% confidence) (UNUSED)
- Line 300: unused function 'cover' (60% confidence) (UNUSED)
- Line 433: unused function 'deform' (60% confidence) (UNUSED)
- Line 453: unused function 'equalize' (60% confidence) (UNUSED)
- Line 636: unused function 'mirror' (60% confidence) (UNUSED)
- Line 646: unused function 'posterize' (60% confidence) (UNUSED)
- Line 659: unused function 'solarize' (60% confidence) (UNUSED)

#### ImagePalette.py
- Line 232: unused function 'make_gamma_lut' (60% confidence) (UNUSED)
- Line 249: unused function 'sepia' (60% confidence) (UNUSED)
- Line 254: unused function 'wedge' (60% confidence) (UNUSED)

#### ImageSequence.py
- Line 64: unused function 'all_frames' (60% confidence) (UNUSED)

#### ImageStat.py
- Line 141: unused method 'rms' (60% confidence) (UNUSED)

#### ImageTransform.py
- Line 46: unused class 'AffineTransform' (60% confidence) (UNUSED)
- Line 67: unused class 'PerspectiveTransform' (60% confidence) (UNUSED)
- Line 109: unused class 'QuadTransform' (60% confidence) (UNUSED)
- Line 126: unused class 'MeshTransform' (60% confidence) (UNUSED)

#### ImageWin.py
- Line 217: unused method 'ui_handle_clear' (60% confidence) (UNUSED)
- Line 220: unused method 'ui_handle_damage' (60% confidence) (UNUSED)
- Line 223: unused method 'ui_handle_destroy' (60% confidence) (UNUSED)
- Line 226: unused method 'ui_handle_repair' (60% confidence) (UNUSED)
- Line 229: unused method 'ui_handle_resize' (60% confidence) (UNUSED)
- Line 236: unused class 'ImageWindow' (60% confidence) (UNUSED)
- Line 246: unused method 'ui_handle_repair' (60% confidence) (UNUSED)

#### ImImagePlugin.py
- Line 121: unused variable 'format_description' (60% confidence) (UNUSED)

#### ImtImagePlugin.py
- Line 34: unused variable 'format_description' (60% confidence) (UNUSED)

#### IptcImagePlugin.py
- Line 72: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 190: unused function 'getiptcinfo' (60% confidence) (UNUSED)

#### Jpeg2KImagePlugin.py
- Line 108: unused variable 'rsiz' (60% confidence) (UNUSED)
- Line 248: unused variable 'format_description' (60% confidence) (UNUSED)

#### JpegImagePlugin.py
- Line 338: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 354: unused attribute '_huffman_dc' (60% confidence) (UNUSED)
- Line 355: unused attribute '_huffman_ac' (60% confidence) (UNUSED)
- Line 465: unused method 'load_djpeg' (60% confidence) (UNUSED)
- Line 858: unused function '_save_cjpeg' (60% confidence) (UNUSED)

#### McIdasImagePlugin.py
- Line 35: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 46: unused attribute 'area_descriptor_raw' (60% confidence) (UNUSED)
- Line 47: unused attribute 'area_descriptor' (60% confidence) (UNUSED)

#### MicImagePlugin.py
- Line 38: unused variable 'format_description' (60% confidence) (UNUSED)

#### MpegImagePlugin.py
- Line 67: unused variable 'format_description' (60% confidence) (UNUSED)

#### MpoImagePlugin.py
- Line 98: unused variable 'format_description' (60% confidence) (UNUSED)

#### MspImagePlugin.py
- Line 50: unused variable 'format_description' (60% confidence) (UNUSED)

#### PalmImagePlugin.py
- Line 98: unused variable 'Palm8BitColormapImage' (60% confidence) (UNUSED)

#### PcdImagePlugin.py
- Line 28: unused variable 'format_description' (60% confidence) (UNUSED)

#### PcfFontFile.py
- Line 36: unused variable 'PCF_ACCELERATORS' (60% confidence) (UNUSED)
- Line 39: unused variable 'PCF_INK_METRICS' (60% confidence) (UNUSED)
- Line 41: unused variable 'PCF_SWIDTHS' (60% confidence) (UNUSED)
- Line 42: unused variable 'PCF_GLYPH_NAMES' (60% confidence) (UNUSED)
- Line 43: unused variable 'PCF_BDF_ACCELERATORS' (60% confidence) (UNUSED)
- Line 57: unused class 'PcfFontFile' (60% confidence) (UNUSED)

#### PcxImagePlugin.py
- Line 51: unused variable 'format_description' (60% confidence) (UNUSED)

#### PdfImagePlugin.py
- Line 234: unused variable 'number_of_pages' (60% confidence) (UNUSED)
- Line 242: unused variable 'number_of_pages' (60% confidence) (UNUSED)

#### PdfParser.py
- Line 233: unused method 'from_pdf_stream' (60% confidence) (UNUSED)
- Line 406: unused attribute 'file_size_this' (60% confidence) (UNUSED)
- Line 581: unused attribute 'file_size_this' (60% confidence) (UNUSED)
- Line 704: unused variable 're_whitespace_optional' (60% confidence) (UNUSED)

#### PixarImagePlugin.py
- Line 40: unused variable 'format_description' (60% confidence) (UNUSED)

#### PngImagePlugin.py
- Line 279: unused class 'PngInfo' (60% confidence) (UNUSED)
- Line 420: unused method 'chunk_iCCP' (60% confidence) (UNUSED)
- Line 448: unused method 'chunk_IHDR' (60% confidence) (UNUSED)
- Line 478: unused attribute 'im_idat' (60% confidence) (UNUSED)
- Line 482: unused method 'chunk_IEND' (60% confidence) (UNUSED)
- Line 486: unused method 'chunk_PLTE' (60% confidence) (UNUSED)
- Line 494: unused method 'chunk_tRNS' (60% confidence) (UNUSED)
- Line 515: unused method 'chunk_gAMA' (60% confidence) (UNUSED)
- Line 522: unused method 'chunk_cHRM' (60% confidence) (UNUSED)
- Line 532: unused method 'chunk_sRGB' (60% confidence) (UNUSED)
- Line 549: unused method 'chunk_pHYs' (60% confidence) (UNUSED)
- Line 567: unused method 'chunk_tEXt' (60% confidence) (UNUSED)
- Line 587: unused method 'chunk_zTXt' (60% confidence) (UNUSED)
- Line 622: unused method 'chunk_iTXt' (60% confidence) (UNUSED)
- Line 665: unused method 'chunk_eXIf' (60% confidence) (UNUSED)
- Line 672: unused method 'chunk_acTL' (60% confidence) (UNUSED)
- Line 693: unused method 'chunk_fcTL' (60% confidence) (UNUSED)
- Line 723: unused method 'chunk_fdAT' (60% confidence) (UNUSED)
- Line 754: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 1517: unused function 'getchunks' (60% confidence) (UNUSED)

#### PpmImagePlugin.py
- Line 59: unused variable 'format_description' (60% confidence) (UNUSED)

#### PsdImagePlugin.py
- Line 60: unused variable 'format_description' (60% confidence) (UNUSED)

#### PSDraw.py
- Line 31: unused class 'PSDraw' (60% confidence) (UNUSED)
- Line 42: unused method 'begin_document' (60% confidence) (UNUSED)
- Line 58: unused method 'end_document' (60% confidence) (UNUSED)
- Line 64: unused method 'setfont' (60% confidence) (UNUSED)
- Line 212: unused variable 'ERROR_PS' (60% confidence) (UNUSED)

#### QoiImagePlugin.py
- Line 22: unused variable 'format_description' (60% confidence) (UNUSED)

#### SgiImagePlugin.py
- Line 54: unused variable 'format_description' (60% confidence) (UNUSED)

#### SpiderImagePlugin.py
- Line 101: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 206: unused method 'tkPhotoImage' (60% confidence) (UNUSED)
- Line 217: unused function 'loadImageSeries' (60% confidence) (UNUSED)

#### SunImagePlugin.py
- Line 34: unused variable 'format_description' (60% confidence) (UNUSED)

#### TarIO.py
- Line 23: unused class 'TarIO' (60% confidence) (UNUSED)

#### TgaImagePlugin.py
- Line 51: unused variable 'format_description' (60% confidence) (UNUSED)

#### TiffImagePlugin.py
- Line 103: unused variable 'PREDICTOR' (60% confidence) (UNUSED)
- Line 112: unused variable 'JPEGTABLES' (60% confidence) (UNUSED)
- Line 124: unused variable 'IMAGEJ_META_DATA_BYTE_COUNTS' (60% confidence) (UNUSED)
- Line 125: unused variable 'IMAGEJ_META_DATA' (60% confidence) (UNUSED)
- Line 802: unused method 'load_byte' (60% confidence) (UNUSED)
- Line 806: unused method 'write_byte' (60% confidence) (UNUSED)
- Line 814: unused method 'load_string' (60% confidence) (UNUSED)
- Line 820: unused method 'write_string' (60% confidence) (UNUSED)
- Line 829: unused method 'load_rational' (60% confidence) (UNUSED)
- Line 840: unused method 'write_rational' (60% confidence) (UNUSED)
- Line 846: unused method 'load_undefined' (60% confidence) (UNUSED)
- Line 850: unused method 'write_undefined' (60% confidence) (UNUSED)
- Line 858: unused method 'load_signed_rational' (60% confidence) (UNUSED)
- Line 869: unused method 'write_signed_rational' (60% confidence) (UNUSED)
- Line 1153: unused variable 'ImageFileDirectory' (60% confidence) (UNUSED)
- Line 1162: unused variable 'format_description' (60% confidence) (UNUSED)
- Line 1275: unused method 'get_photoshop_blocks' (60% confidence) (UNUSED)
- Line 2141: unused attribute 'longFmt' (60% confidence) (UNUSED)
- Line 2142: unused attribute 'shortFmt' (60% confidence) (UNUSED)
- Line 2174: unused method 'readShort' (60% confidence) (UNUSED)
- Line 2177: unused method 'readLong' (60% confidence) (UNUSED)
- Line 2197: unused method 'rewriteLastShortToLong' (60% confidence) (UNUSED)
- Line 2200: unused method 'rewriteLastShort' (60% confidence) (UNUSED)
- Line 2203: unused method 'rewriteLastLong' (60% confidence) (UNUSED)
- Line 2215: unused method 'writeLong' (60% confidence) (UNUSED)
- Line 2292: unused method 'fixOffsets' (60% confidence) (UNUSED)

#### WalImageFile.py
- Line 36: unused variable 'format_description' (60% confidence) (UNUSED)

#### WebPImagePlugin.py
- Line 39: unused variable 'format_description' (60% confidence) (UNUSED)

#### WmfImagePlugin.py
- Line 80: unused variable 'format_description' (60% confidence) (UNUSED)

#### XbmImagePlugin.py
- Line 50: unused variable 'format_description' (60% confidence) (UNUSED)

#### XpmImagePlugin.py
- Line 37: unused variable 'format_description' (60% confidence) (UNUSED)

#### XVThumbImagePlugin.py
- Line 46: unused variable 'format_description' (60% confidence) (UNUSED)

#### parser.py
- Line 28: unused method 'format_option_strings' (60% confidence) (UNUSED)
- Line 57: unused method 'format_heading' (60% confidence) (UNUSED)
- Line 70: unused method 'format_description' (60% confidence) (UNUSED)

#### cache.py
- Line 15: unused class 'CacheCommand' (60% confidence) (UNUSED)

#### check.py
- Line 17: unused class 'CheckCommand' (60% confidence) (UNUSED)

#### completion.py
- Line 75: unused class 'CompletionCommand' (60% confidence) (UNUSED)

#### configuration.py
- Line 22: unused class 'ConfigurationCommand' (60% confidence) (UNUSED)

#### debug.py
- Line 158: unused class 'DebugCommand' (60% confidence) (UNUSED)

#### download.py
- Line 18: unused class 'DownloadCommand' (60% confidence) (UNUSED)

#### freeze.py
- Line 25: unused class 'FreezeCommand' (60% confidence) (UNUSED)

#### hash.py
- Line 15: unused class 'HashCommand' (60% confidence) (UNUSED)

#### help.py
- Line 9: unused class 'HelpCommand' (60% confidence) (UNUSED)

#### index.py
- Line 22: unused class 'IndexCommand' (60% confidence) (UNUSED)

#### inspect.py
- Line 19: unused class 'InspectCommand' (60% confidence) (UNUSED)

#### install.py
- Line 52: unused class 'InstallCommand' (60% confidence) (UNUSED)

#### list.py
- Line 39: unused class 'ListCommand' (60% confidence) (UNUSED)

#### search.py
- Line 25: unused class 'TransformedHit' (60% confidence) (UNUSED)
- Line 34: unused class 'SearchCommand' (60% confidence) (UNUSED)

#### show.py
- Line 15: unused class 'ShowCommand' (60% confidence) (UNUSED)

#### uninstall.py
- Line 25: unused class 'UninstallCommand' (60% confidence) (UNUSED)

#### wheel.py
- Line 24: unused class 'WheelCommand' (60% confidence) (UNUSED)

#### collector.py
- Line 298: unused method 'handle_starttag' (60% confidence) (UNUSED)

#### xmlrpc.py
- Line 14: unused import '_HostType' (90% confidence) (UNUSED)
- Line 14: unused import '_Marshallable' (90% confidence) (UNUSED)
- Line 16: unused import 'SizedBuffer' (90% confidence) (UNUSED)

#### req_install.py
- Line 229: unused method 'format_debug' (60% confidence) (UNUSED)

#### factory.py
- Line 75: unused class 'ConflictCause' (60% confidence) (UNUSED)

#### provider.py
- Line 21: unused import 'Preference' (90% confidence) (UNUSED)
- Line 24: unused variable 'PreferenceInformation' (60% confidence) (UNUSED)

#### datetime.py
- Line 7: unused function 'today_is_later_than' (60% confidence) (UNUSED)

#### logging.py
- Line 74: unused variable 'default_time_format' (60% confidence) (UNUSED)
- Line 140: unused class 'RichPipStreamHandler' (60% confidence) (UNUSED)
- Line 200: unused class 'BetterRotatingFileHandler' (60% confidence) (UNUSED)
- Line 206: unused class 'MaxLevelFilter' (60% confidence) (UNUSED)
- Line 214: unused class 'ExcludeLoggerFilter' (60% confidence) (UNUSED)

#### misc.py
- Line 429: unused function 'captured_stderr' (60% confidence) (UNUSED)

#### versioncontrol.py
- Line 263: unused method 'get_backend' (60% confidence) (UNUSED)

#### file_cache.py
- Line 175: unused function 'url_to_file_path' (60% confidence) (UNUSED)

#### heuristics.py
- Line 60: unused class 'OneDayCache' (60% confidence) (UNUSED)
- Line 94: unused class 'LastModified' (60% confidence) (UNUSED)

#### serialize.py
- Line 152: unused method '_loads_v0' (60% confidence) (UNUSED)
- Line 163: unused method '_loads_v1' (60% confidence) (UNUSED)
- Line 173: unused method '_loads_v2' (60% confidence) (UNUSED)
- Line 184: unused method '_loads_v3' (60% confidence) (UNUSED)
- Line 195: unused method '_loads_v4' (60% confidence) (UNUSED)

#### codingstatemachine.py
- Line 59: unused attribute '_curr_byte_pos' (60% confidence) (UNUSED)
- Line 74: unused attribute '_curr_byte_pos' (60% confidence) (UNUSED)
- Line 79: unused attribute '_curr_byte_pos' (60% confidence) (UNUSED)

#### codingstatemachinedict.py
- Line 11: unused variable 'class_table' (60% confidence) (UNUSED)
- Line 12: unused variable 'class_factor' (60% confidence) (UNUSED)
- Line 13: unused variable 'state_table' (60% confidence) (UNUSED)
- Line 14: unused variable 'char_len_table' (60% confidence) (UNUSED)

#### enums.py
- Line 34: unused variable 'CJK' (60% confidence) (UNUSED)
- Line 62: unused variable 'NEGATIVE' (60% confidence) (UNUSED)
- Line 63: unused variable 'UNLIKELY' (60% confidence) (UNUSED)
- Line 82: unused variable 'LINE_BREAK' (60% confidence) (UNUSED)
- Line 84: unused variable 'DIGIT' (60% confidence) (UNUSED)

#### hebrewprober.py
- Line 144: unused variable 'NORMAL_TSADI' (60% confidence) (UNUSED)

#### langhungarianmodel.py
- Line 4372: unused variable 'WINDOWS_1250_HUNGARIAN_MODEL' (60% confidence) (UNUSED)
- Line 4641: unused variable 'ISO_8859_2_HUNGARIAN_MODEL' (60% confidence) (UNUSED)

#### mbcssm.py
- Line 520: unused variable 'UCS2BE_SM_MODEL' (60% confidence) (UNUSED)
- Line 578: unused variable 'UCS2LE_SM_MODEL' (60% confidence) (UNUSED)

#### languages.py
- Line 66: unused variable 'LANGUAGES' (60% confidence) (UNUSED)

#### ansi.py
- Line 18: unused function 'clear_screen' (60% confidence) (UNUSED)
- Line 21: unused function 'clear_line' (60% confidence) (UNUSED)
- Line 41: unused method 'FORWARD' (60% confidence) (UNUSED)
- Line 43: unused method 'BACK' (60% confidence) (UNUSED)
- Line 45: unused method 'POS' (60% confidence) (UNUSED)

#### initialise.py
- Line 95: unused function 'colorama_text' (60% confidence) (UNUSED)
- Line 104: unused function 'reinit' (60% confidence) (UNUSED)

#### ansi_test.py
- Line 25: unused method 'testForeAttributes' (60% confidence) (UNUSED)
- Line 47: unused method 'testBackAttributes' (60% confidence) (UNUSED)
- Line 69: unused method 'testStyleAttributes' (60% confidence) (UNUSED)

#### ansitowin32_test.py
- Line 22: unused method 'testIsAProxy' (60% confidence) (UNUSED)
- Line 27: unused method 'testDelegatesWrite' (60% confidence) (UNUSED)
- Line 34: unused method 'testDelegatesContext' (60% confidence) (UNUSED)
- Line 41: unused method 'testProxyNoContextManager' (60% confidence) (UNUSED)
- Line 63: unused method 'testInit' (60% confidence) (UNUSED)
- Line 70: unused method 'testStripIsTrueOnWindows' (60% confidence) (UNUSED)
- Line 78: unused method 'testStripIsFalseOffWindows' (60% confidence) (UNUSED)
- Line 84: unused method 'testWriteStripsAnsi' (60% confidence) (UNUSED)
- Line 96: unused method 'testWriteDoesNotStripAnsi' (60% confidence) (UNUSED)
- Line 120: unused method 'testWriteAutoresets' (60% confidence) (UNUSED)
- Line 126: unused method 'testWriteAndConvertWritesPlainText' (60% confidence) (UNUSED)
- Line 131: unused method 'testWriteAndConvertStripsAllValidAnsi' (60% confidence) (UNUSED)
- Line 157: unused method 'testWriteAndConvertSkipsEmptySnippets' (60% confidence) (UNUSED)
- Line 163: unused method 'testWriteAndConvertCallsWin32WithParamsAndCommand' (60% confidence) (UNUSED)
- Line 205: unused method 'testExtractParams' (60% confidence) (UNUSED)
- Line 219: unused method 'testCallWin32UsesLookup' (60% confidence) (UNUSED)

#### initialise_test.py
- Line 42: unused method 'testInitWrapsOnWindows' (60% confidence) (UNUSED)
- Line 50: unused method 'testInitDoesntWrapOnEmulatedWindows' (60% confidence) (UNUSED)
- Line 57: unused method 'testInitDoesntWrapOnNonWindows' (60% confidence) (UNUSED)
- Line 62: unused method 'testInitDoesntWrapIfNone' (60% confidence) (UNUSED)
- Line 70: unused method 'testInitAutoresetOnWrapsOnAllPlatforms' (60% confidence) (UNUSED)
- Line 75: unused method 'testInitWrapOffDoesntWrapOnWindows' (60% confidence) (UNUSED)
- Line 80: unused method 'testInitWrapOffIncompatibleWithAutoresetOn' (60% confidence) (UNUSED)
- Line 83: unused method 'testAutoResetPassedOn' (60% confidence) (UNUSED)
- Line 92: unused method 'testAutoResetChangeable' (60% confidence) (UNUSED)
- Line 110: unused method 'testAtexitRegisteredOnlyOnce' (60% confidence) (UNUSED)
- Line 128: unused method 'testJustFixWindowsConsole' (60% confidence) (UNUSED)

#### winterm_test.py
- Line 15: unused method 'testInit' (60% confidence) (UNUSED)
- Line 25: unused method 'testGetAttrs' (60% confidence) (UNUSED)
- Line 47: unused method 'testResetAll' (60% confidence) (UNUSED)
- Line 66: unused method 'testFore' (60% confidence) (UNUSED)
- Line 77: unused method 'testBack' (60% confidence) (UNUSED)
- Line 88: unused method 'testStyle' (60% confidence) (UNUSED)
- Line 99: unused method 'testSetConsole' (60% confidence) (UNUSED)
- Line 114: unused method 'testSetConsoleOnStderr' (60% confidence) (UNUSED)

#### __init__.py
- Line 28: unused method 'createLock' (60% confidence) (UNUSED)

#### compat.py
- Line 27: unused import 'ContentTooShortError' (90% confidence) (UNUSED)
- Line 27: unused import 'splittype' (90% confidence) (UNUSED)
- Line 35: unused import 'urllib2' (90% confidence) (UNUSED)
- Line 45: unused import 'htmlentitydefs' (90% confidence) (UNUSED)
- Line 70: unused import 'splittype' (90% confidence) (UNUSED)
- Line 78: unused import 'ContentTooShortError' (90% confidence) (UNUSED)
- Line 80: unused import 'urllib2' (90% confidence) (UNUSED)
- Line 84: unused import 'htmlentitydefs' (90% confidence) (UNUSED)
- Line 898: unused method 'viewkeys' (60% confidence) (UNUSED)
- Line 902: unused method 'viewvalues' (60% confidence) (UNUSED)
- Line 906: unused method 'viewitems' (60% confidence) (UNUSED)
- Line 1052: unused method 'ext_convert' (60% confidence) (UNUSED)
- Line 1056: unused method 'cfg_convert' (60% confidence) (UNUSED)

#### database.py
- Line 36: unused variable 'COMMANDS_FILENAME' (60% confidence) (UNUSED)
- Line 258: unused method 'provides_distribution' (60% confidence) (UNUSED)
- Line 299: unused method 'get_file_path' (60% confidence) (UNUSED)
- Line 308: unused method 'get_exported_entries' (60% confidence) (UNUSED)
- Line 410: unused property 'test_requires' (60% confidence) (UNUSED)
- Line 418: unused method 'matches_requirement' (60% confidence) (UNUSED)
- Line 717: unused method 'check_installed_files' (60% confidence) (UNUSED)
- Line 753: unused method 'shared_locations' (60% confidence) (UNUSED)
- Line 843: unused method 'list_distinfo_files' (60% confidence) (UNUSED)
- Line 874: unused variable 'shared_locations' (60% confidence) (UNUSED)
- Line 999: unused method 'check_installed_files' (60% confidence) (UNUSED)
- Line 1056: unused method 'list_distinfo_files' (60% confidence) (UNUSED)
- Line 1202: unused method 'topological_sort' (60% confidence) (UNUSED)
- Line 1295: unused function 'get_dependent_dists' (60% confidence) (UNUSED)
- Line 1321: unused function 'get_required_dists' (60% confidence) (UNUSED)

#### index.py
- Line 87: unused method 'save_configuration' (60% confidence) (UNUSED)
- Line 289: unused method 'upload_documentation' (60% confidence) (UNUSED)
- Line 341: unused method 'verify_signature' (60% confidence) (UNUSED)
- Line 365: unused method 'download_file' (60% confidence) (UNUSED)

#### locators.py
- Line 42: unused function 'get_all_distribution_names' (60% confidence) (UNUSED)
- Line 86: unused variable 'http_error_301' (60% confidence) (UNUSED)
- Line 86: unused variable 'http_error_303' (60% confidence) (UNUSED)
- Line 86: unused variable 'http_error_307' (60% confidence) (UNUSED)
- Line 902: unused class 'JSONLocator' (60% confidence) (UNUSED)
- Line 1069: unused class 'DependencyFinder' (60% confidence) (UNUSED)

#### manifest.py
- Line 96: unused method 'add_many' (60% confidence) (UNUSED)
- Line 132: unused method 'process_directive' (60% confidence) (UNUSED)

#### metadata.py
- Line 115: unused variable 'EXTRA_RE' (60% confidence) (UNUSED)
- Line 262: unused attribute 'requires_files' (60% confidence) (UNUSED)
- Line 335: unused method 'is_multi_field' (60% confidence) (UNUSED)
- Line 700: unused variable 'common_keys' (60% confidence) (UNUSED)
- Line 705: unused variable 'mapped_keys' (60% confidence) (UNUSED)

#### scripts.py
- Line 247: unused method 'get_manifest' (60% confidence) (UNUSED)

#### util.py
- Line 280: unused function 'get_resources_dests' (60% confidence) (UNUSED)
- Line 334: unused function 'proceed' (60% confidence) (UNUSED)
- Line 575: unused method 'write_text_file' (60% confidence) (UNUSED)
- Line 650: unused method 'is_writable' (60% confidence) (UNUSED)
- Line 836: unused function 'parse_credentials' (60% confidence) (UNUSED)
- Line 851: unused function 'get_process_umask' (60% confidence) (UNUSED)
- Line 857: unused function 'is_string_sequence' (60% confidence) (UNUSED)
- Line 979: unused function 'get_package_data' (60% confidence) (UNUSED)
- Line 1029: unused class 'EventMixin' (60% confidence) (UNUSED)
- Line 1076: unused method 'publish' (60% confidence) (UNUSED)
- Line 1103: unused class 'Sequencer' (60% confidence) (UNUSED)
- Line 1151: unused method 'get_steps' (60% confidence) (UNUSED)
- Line 1176: unused property 'strong_connections' (60% confidence) (UNUSED)
- Line 1249: unused function 'unarchive' (60% confidence) (UNUSED)
- Line 1396: unused property 'ETA' (60% confidence) (UNUSED)
- Line 1541: unused method 'https_open' (60% confidence) (UNUSED)
- Line 1561: unused class 'HTTPSOnlyHandler' (60% confidence) (UNUSED)
- Line 1563: unused method 'http_open' (60% confidence) (UNUSED)
- Line 1578: unused method 'make_connection' (60% confidence) (UNUSED)
- Line 1581: unused attribute '_extra_headers' (60% confidence) (UNUSED)
- Line 1594: unused method 'make_connection' (60% confidence) (UNUSED)
- Line 1600: unused attribute '_extra_headers' (60% confidence) (UNUSED)
- Line 1752: unused method 'inc_convert' (60% confidence) (UNUSED)
- Line 1761: unused class 'SubprocessMixin' (60% confidence) (UNUSED)

#### version.py
- Line 150: unused property 'exact_version' (60% confidence) (UNUSED)
- Line 332: unused method '_match_lt' (60% confidence) (UNUSED)
- Line 340: unused method '_match_gt' (60% confidence) (UNUSED)
- Line 348: unused method '_match_le' (60% confidence) (UNUSED)
- Line 352: unused method '_match_ge' (60% confidence) (UNUSED)
- Line 356: unused method '_match_eq' (60% confidence) (UNUSED)
- Line 364: unused method '_match_arbitrary' (60% confidence) (UNUSED)
- Line 367: unused method '_match_ne' (60% confidence) (UNUSED)
- Line 375: unused method '_match_compatible' (60% confidence) (UNUSED)
- Line 637: unused method '_match_compatible' (60% confidence) (UNUSED)

#### wheel.py
- Line 188: unused attribute 'should_verify' (60% confidence) (UNUSED)
- Line 822: unused method 'unmount' (60% confidence) (UNUSED)

#### distro.py
- Line 1115: unused attribute 'whitespace_split' (60% confidence) (UNUSED)

#### codec.py
- Line 29: unused method '_buffer_encode' (60% confidence) (UNUSED)
- Line 62: unused method '_buffer_decode' (60% confidence) (UNUSED)
- Line 102: unused function 'getregentry' (60% confidence) (UNUSED)

#### compat.py
- Line 5: unused function 'ToASCII' (60% confidence) (UNUSED)
- Line 8: unused function 'ToUnicode' (60% confidence) (UNUSED)
- Line 11: unused function 'nameprep' (60% confidence) (UNUSED)

#### intranges.py
- Line 11: unused function 'intranges_from_list' (60% confidence) (UNUSED)

#### exceptions.py
- Line 46: unused variable 'PackException' (60% confidence) (UNUSED)
- Line 47: unused variable 'PackValueError' (60% confidence) (UNUSED)
- Line 48: unused variable 'PackOverflowError' (60% confidence) (UNUSED)

#### ext.py
- Line 157: unused method 'from_unix_nano' (60% confidence) (UNUSED)

#### fallback.py
- Line 648: unused method 'read_array_header' (60% confidence) (UNUSED)
- Line 653: unused method 'read_map_header' (60% confidence) (UNUSED)
- Line 892: unused method 'pack_map_pairs' (60% confidence) (UNUSED)
- Line 899: unused method 'pack_array_header' (60% confidence) (UNUSED)
- Line 908: unused method 'pack_map_header' (60% confidence) (UNUSED)
- Line 917: unused method 'pack_ext_type' (60% confidence) (UNUSED)

#### _manylinux.py
- Line 28: unused variable 'EM_S390' (60% confidence) (UNUSED)
- Line 30: unused variable 'EM_X86_64' (60% confidence) (UNUSED)
- Line 53: unused attribute 'e_ident_version' (60% confidence) (UNUSED)
- Line 54: unused attribute 'e_ident_osabi' (60% confidence) (UNUSED)
- Line 55: unused attribute 'e_ident_abiversion' (60% confidence) (UNUSED)
- Line 56: unused attribute 'e_ident_pad' (60% confidence) (UNUSED)
- Line 61: unused attribute 'e_type' (60% confidence) (UNUSED)
- Line 63: unused attribute 'e_version' (60% confidence) (UNUSED)
- Line 64: unused attribute 'e_entry' (60% confidence) (UNUSED)
- Line 66: unused attribute 'e_shoff' (60% confidence) (UNUSED)
- Line 68: unused attribute 'e_ehsize' (60% confidence) (UNUSED)
- Line 71: unused attribute 'e_shentsize' (60% confidence) (UNUSED)
- Line 72: unused attribute 'e_shnum' (60% confidence) (UNUSED)
- Line 73: unused attribute 'e_shstrndx' (60% confidence) (UNUSED)

#### specifiers.py
- Line 269: unused method '_compare_not_equal' (60% confidence) (UNUSED)
- Line 272: unused method '_compare_less_than_equal' (60% confidence) (UNUSED)
- Line 275: unused method '_compare_greater_than_equal' (60% confidence) (UNUSED)
- Line 280: unused method '_compare_less_than' (60% confidence) (UNUSED)
- Line 283: unused method '_compare_greater_than' (60% confidence) (UNUSED)
- Line 407: unused method '_compare_compatible' (60% confidence) (UNUSED)
- Line 469: unused method '_compare_not_equal' (60% confidence) (UNUSED)
- Line 473: unused method '_compare_less_than_equal' (60% confidence) (UNUSED)
- Line 481: unused method '_compare_greater_than_equal' (60% confidence) (UNUSED)
- Line 491: unused method '_compare_less_than' (60% confidence) (UNUSED)
- Line 517: unused method '_compare_greater_than' (60% confidence) (UNUSED)
- Line 549: unused method '_compare_arbitrary' (60% confidence) (UNUSED)

#### version.py
- Line 33: unused variable 'VersionComparisonMethod' (60% confidence) (UNUSED)
- Line 163: unused property 'is_devrelease' (60% confidence) (UNUSED)
- Line 376: unused property 'is_devrelease' (60% confidence) (UNUSED)

#### __init__.py
- Line 102: unused variable 'resources_stream' (60% confidence) (UNUSED)
- Line 104: unused variable 'resource_dir' (60% confidence) (UNUSED)
- Line 162: unused function '_sget_dict' (60% confidence) (UNUSED)
- Line 166: unused function '_sset_dict' (60% confidence) (UNUSED)
- Line 171: unused function '_sget_object' (60% confidence) (UNUSED)
- Line 175: unused function '_sset_object' (60% confidence) (UNUSED)
- Line 360: unused property 'requirers_str' (60% confidence) (UNUSED)
- Line 3094: unused variable 'EQEQ' (60% confidence) (UNUSED)
- Line 3167: unused class 'RequirementParseError' (60% confidence) (UNUSED)
- Line 3327: unused function '_initialize_master_working_set' (60% confidence) (UNUSED)

#### console.py
- Line 40: unused function 'reset_color' (60% confidence) (UNUSED)

#### formatter.py
- Line 81: unused variable 'unicodeoutput' (60% confidence) (UNUSED)

#### img.py
- Line 349: unused variable 'unicodeoutput' (60% confidence) (UNUSED)
- Line 425: unused method '_get_char_width' (60% confidence) (UNUSED)

#### irc.py
- Line 94: unreachable code after 'return' (100% confidence) (UNUSED)

#### other.py
- Line 60: unused variable 'unicodeoutput' (60% confidence) (UNUSED)

#### lexer.py
- Line 868: unused variable 'it_index' (60% confidence) (UNUSED)
- Line 917: unused class 'ProfilingRegexLexer' (60% confidence) (UNUSED)

#### __init__.py
- Line 82: unused function 'find_lexer_class_by_name' (60% confidence) (UNUSED)

#### python.py
- Line 414: unused variable 'Python3Lexer' (60% confidence) (UNUSED)
- Line 774: unused variable 'Python3TracebackLexer' (60% confidence) (UNUSED)

#### regexopt.py
- Line 19: unused variable 'FIRST_ELEMENT' (60% confidence) (UNUSED)

#### sphinxext.py
- Line 63: unused variable 'has_content' (60% confidence) (UNUSED)
- Line 64: unused variable 'required_arguments' (60% confidence) (UNUSED)
- Line 65: unused variable 'optional_arguments' (60% confidence) (UNUSED)
- Line 66: unused variable 'final_argument_whitespace' (60% confidence) (UNUSED)
- Line 67: unused variable 'option_spec' (60% confidence) (UNUSED)

#### style.py
- Line 156: unused function 'list_styles' (60% confidence) (UNUSED)
- Line 197: unused variable 'web_style_gallery_exclude' (60% confidence) (UNUSED)

#### token.py
- Line 85: unused function 'is_token_subtype' (60% confidence) (UNUSED)

#### unistring.py
- Line 14: unused variable 'Cc' (60% confidence) (UNUSED)
- Line 16: unused variable 'Cf' (60% confidence) (UNUSED)
- Line 18: unused variable 'Cn' (60% confidence) (UNUSED)
- Line 20: unused variable 'Co' (60% confidence) (UNUSED)
- Line 22: unused variable 'Cs' (60% confidence) (UNUSED)
- Line 26: unused variable 'Lm' (60% confidence) (UNUSED)
- Line 28: unused variable 'Lo' (60% confidence) (UNUSED)
- Line 34: unused variable 'Mc' (60% confidence) (UNUSED)
- Line 36: unused variable 'Me' (60% confidence) (UNUSED)
- Line 38: unused variable 'Mn' (60% confidence) (UNUSED)
- Line 40: unused variable 'Nd' (60% confidence) (UNUSED)
- Line 42: unused variable 'Nl' (60% confidence) (UNUSED)
- Line 44: unused variable 'No' (60% confidence) (UNUSED)
- Line 46: unused variable 'Pc' (60% confidence) (UNUSED)
- Line 48: unused variable 'Pd' (60% confidence) (UNUSED)
- Line 50: unused variable 'Pe' (60% confidence) (UNUSED)
- Line 52: unused variable 'Pf' (60% confidence) (UNUSED)
- Line 54: unused variable 'Pi' (60% confidence) (UNUSED)
- Line 56: unused variable 'Po' (60% confidence) (UNUSED)
- Line 58: unused variable 'Ps' (60% confidence) (UNUSED)
- Line 60: unused variable 'Sc' (60% confidence) (UNUSED)
- Line 62: unused variable 'Sk' (60% confidence) (UNUSED)
- Line 64: unused variable 'Sm' (60% confidence) (UNUSED)
- Line 66: unused variable 'So' (60% confidence) (UNUSED)
- Line 68: unused variable 'Zl' (60% confidence) (UNUSED)
- Line 70: unused variable 'Zp' (60% confidence) (UNUSED)
- Line 72: unused variable 'Zs' (60% confidence) (UNUSED)

#### __init__.py
- Line 154: unused variable 'core_builtin_exprs' (60% confidence) (UNUSED)

#### common.py
- Line 167: unused variable 'hex_integer' (60% confidence) (UNUSED)
- Line 212: unused variable 'fnumber' (60% confidence) (UNUSED)
- Line 240: unused variable 'ipv6_address' (60% confidence) (UNUSED)
- Line 247: unused variable 'mac_address' (60% confidence) (UNUSED)
- Line 306: unused variable 'iso8601_date' (60% confidence) (UNUSED)
- Line 311: unused variable 'iso8601_datetime' (60% confidence) (UNUSED)
- Line 414: unused variable 'convertToInteger' (60% confidence) (UNUSED)
- Line 416: unused variable 'convertToFloat' (60% confidence) (UNUSED)
- Line 418: unused variable 'convertToDate' (60% confidence) (UNUSED)
- Line 420: unused variable 'convertToDatetime' (60% confidence) (UNUSED)
- Line 422: unused variable 'stripHTMLTags' (60% confidence) (UNUSED)
- Line 424: unused variable 'upcaseTokens' (60% confidence) (UNUSED)
- Line 426: unused variable 'downcaseTokens' (60% confidence) (UNUSED)

#### core.py
- Line 172: unused function 'enable_diag' (60% confidence) (UNUSED)
- Line 179: unused function 'disable_diag' (60% confidence) (UNUSED)
- Line 202: unused variable 'w_line' (60% confidence) (UNUSED)
- Line 236: unused variable 'ParseImplReturnType' (60% confidence) (UNUSED)
- Line 237: unused variable 'PostParseReturnType' (60% confidence) (UNUSED)
- Line 444: unused method 'using_each' (60% confidence) (UNUSED)
- Line 807: unused variable 'MATCH' (60% confidence) (UNUSED)
- Line 961: unused variable 'MATCH' (60% confidence) (UNUSED)
- Line 2192: unused method 'create_diagram' (60% confidence) (UNUSED)
- Line 2253: unused method 'setDefaultWhitespaceChars' (60% confidence) (UNUSED)
- Line 2257: unused method 'setResultsName' (60% confidence) (UNUSED)
- Line 2260: unused method 'setBreak' (60% confidence) (UNUSED)
- Line 2266: unused method 'addParseAction' (60% confidence) (UNUSED)
- Line 2269: unused method 'addCondition' (60% confidence) (UNUSED)
- Line 2272: unused method 'setFailAction' (60% confidence) (UNUSED)
- Line 2278: unused method 'enableLeftRecursion' (60% confidence) (UNUSED)
- Line 2282: unused method 'enablePackrat' (60% confidence) (UNUSED)
- Line 2289: unused method 'scanString' (60% confidence) (UNUSED)
- Line 2292: unused method 'transformString' (60% confidence) (UNUSED)
- Line 2295: unused method 'searchString' (60% confidence) (UNUSED)
- Line 2298: unused method 'ignoreWhitespace' (60% confidence) (UNUSED)
- Line 2304: unused method 'setWhitespaceChars' (60% confidence) (UNUSED)
- Line 2307: unused method 'parseWithTabs' (60% confidence) (UNUSED)
- Line 2310: unused method 'setDebugActions' (60% confidence) (UNUSED)
- Line 2313: unused method 'setDebug' (60% confidence) (UNUSED)
- Line 2319: unused method 'parseFile' (60% confidence) (UNUSED)
- Line 2322: unused method 'runTests' (60% confidence) (UNUSED)
- Line 2594: unused variable 'setDefaultKeywordChars' (60% confidence) (UNUSED)
- Line 2839: unused attribute 'bodyCharsOrig' (60% confidence) (UNUSED)
- Line 2842: unused attribute 'bodyCharsOrig' (60% confidence) (UNUSED)
- Line 3896: unused method 'ignoreWhitespace' (60% confidence) (UNUSED)
- Line 4619: unused method 'ignoreWhitespace' (60% confidence) (UNUSED)
- Line 5628: unused method 'ignoreWhitespace' (60% confidence) (UNUSED)
- Line 6066: unused variable 'python_quoted_string' (60% confidence) (UNUSED)

#### __init__.py
- Line 324: unused attribute 'extracted_diagram_names' (60% confidence) (UNUSED)
- Line 338: unused method 'generate_unnamed' (60% confidence) (UNUSED)

#### exceptions.py
- Line 247: unused method 'markInputline' (60% confidence) (UNUSED)

#### helpers.py
- Line 595: unused attribute 'tag_body' (60% confidence) (UNUSED)

#### results.py
- Line 175: unused attribute '_modal' (60% confidence) (UNUSED)
- Line 789: unused variable 'asDict' (60% confidence) (UNUSED)

#### testing.py
- Line 20: unused class 'reset_pyparsing_context' (60% confidence) (UNUSED)
- Line 141: unused method 'assertParseAndCheckList' (60% confidence) (UNUSED)
- Line 155: unused method 'assertParseAndCheckDict' (60% confidence) (UNUSED)
- Line 169: unused method 'assertRunTestResults' (60% confidence) (UNUSED)
- Line 232: unused method 'assertRaisesParseException' (60% confidence) (UNUSED)

#### unicode.py
- Line 277: unused variable '漢字' (60% confidence) (UNUSED)
- Line 278: unused variable 'カタカナ' (60% confidence) (UNUSED)
- Line 279: unused variable 'ひらがな' (60% confidence) (UNUSED)
- Line 309: unused class 'CJK' (60% confidence) (UNUSED)
- Line 348: unused variable 'BMP' (60% confidence) (UNUSED)
- Line 351: unused variable 'العربية' (60% confidence) (UNUSED)
- Line 352: unused variable '中文' (60% confidence) (UNUSED)
- Line 353: unused variable 'кириллица' (60% confidence) (UNUSED)
- Line 354: unused variable 'Ελληνικά' (60% confidence) (UNUSED)
- Line 355: unused variable 'עִברִית' (60% confidence) (UNUSED)
- Line 356: unused variable '日本語' (60% confidence) (UNUSED)
- Line 357: unused variable '한국어' (60% confidence) (UNUSED)
- Line 358: unused variable 'ไทย' (60% confidence) (UNUSED)
- Line 359: unused variable 'देवनागरी' (60% confidence) (UNUSED)

#### _internal_utils.py
- Line 19: unused variable 'HEADER_VALIDATORS' (60% confidence) (UNUSED)

#### adapters.py
- Line 67: unused variable 'DEFAULT_POOL_TIMEOUT' (60% confidence) (UNUSED)

#### auth.py
- Line 21: unused variable 'CONTENT_TYPE_FORM_URLENCODED' (60% confidence) (UNUSED)
- Line 22: unused variable 'CONTENT_TYPE_MULTI_PART' (60% confidence) (UNUSED)
- Line 99: unused class 'HTTPProxyAuth' (60% confidence) (UNUSED)
- Line 107: unused class 'HTTPDigestAuth' (60% confidence) (UNUSED)

#### compat.py
- Line 22: unused variable 'is_py2' (60% confidence) (UNUSED)
- Line 25: unused variable 'is_py3' (60% confidence) (UNUSED)

#### cookies.py
- Line 72: unused method 'has_header' (60% confidence) (UNUSED)
- Line 90: unused property 'unverifiable' (60% confidence) (UNUSED)
- Line 94: unused property 'origin_req_host' (60% confidence) (UNUSED)
- Line 277: unused method 'list_domains' (60% confidence) (UNUSED)
- Line 285: unused method 'list_paths' (60% confidence) (UNUSED)
- Line 293: unused method 'multiple_domains' (60% confidence) (UNUSED)
- Line 426: unused attribute '_cookies_lock' (60% confidence) (UNUSED)

#### exceptions.py
- Line 81: unused class 'URLRequired' (60% confidence) (UNUSED)

#### models.py
- Line 218: unused method 'deregister_hook' (60% confidence) (UNUSED)
- Line 777: unused property 'is_permanent_redirect' (60% confidence) (UNUSED)

#### structures.py
- Line 58: unused variable 'mappedvalue' (60% confidence) (UNUSED)

#### utils.py
- Line 124: unused function 'dict_to_sequence' (60% confidence) (UNUSED)
- Line 313: unused function 'from_key_val_list' (60% confidence) (UNUSED)
- Line 370: unused function 'parse_list_header' (60% confidence) (UNUSED)
- Line 462: unused function 'dict_from_cookiejar' (60% confidence) (UNUSED)
- Line 477: unused function 'add_dict_to_cookiejar' (60% confidence) (UNUSED)
- Line 488: unused function 'get_encodings_from_content' (60% confidence) (UNUSED)
- Line 590: unused function 'get_unicode_from_response' (60% confidence) (UNUSED)

#### providers.py
- Line 115: unused variable 'base_exception' (60% confidence) (UNUSED)

#### resolvers.py
- Line 515: unused variable 'base_exception' (60% confidence) (UNUSED)

#### structs.py
- Line 60: unused method 'iter_edges' (60% confidence) (UNUSED)
- Line 68: unused method 'iter_parents' (60% confidence) (UNUSED)

#### _inspect.py
- Line 260: unused function 'is_object_one_of_types' (60% confidence) (UNUSED)

#### _null_file.py
- Line 12: unused variable '__n' (100% confidence) (UNUSED)
- Line 18: unused variable '__limit' (100% confidence) (UNUSED)
- Line 21: unused variable '__hint' (100% confidence) (UNUSED)
- Line 24: unused variable '__whence' (100% confidence) (UNUSED)
- Line 39: unused variable '__lines' (100% confidence) (UNUSED)
- Line 53: unused variable '__t' (100% confidence) (UNUSED)

#### align.py
- Line 234: unused class 'VerticalCenter' (60% confidence) (UNUSED)

#### box.py
- Line 313: unused variable 'SIMPLE_HEAD' (60% confidence) (UNUSED)
- Line 341: unused variable 'HORIZONTALS' (60% confidence) (UNUSED)
- Line 419: unused variable 'DOUBLE_EDGE' (60% confidence) (UNUSED)
- Line 432: unused variable 'MARKDOWN' (60% confidence) (UNUSED)

#### color.py
- Line 571: unused function 'parse_rgb_hex' (60% confidence) (UNUSED)

#### console.py
- Line 1783: unused method 'update_screen' (60% confidence) (UNUSED)
- Line 2158: unused method 'save_text' (60% confidence) (UNUSED)
- Line 2529: unused method 'save_svg' (60% confidence) (UNUSED)
- Line 2568: unused function '_svg_hash' (60% confidence) (UNUSED)

#### control.py
- Line 113: unused method 'move_to_column' (60% confidence) (UNUSED)

#### emoji.py
- Line 27: unused class 'Emoji' (60% confidence) (UNUSED)

#### errors.py
- Line 17: unused class 'StyleStackError' (60% confidence) (UNUSED)

#### highlighter.py
- Line 143: unused class 'ISO8601Highlighter' (60% confidence) (UNUSED)

#### layout.py
- Line 287: unused method 'add_split' (60% confidence) (UNUSED)
- Line 316: unused method 'unsplit' (60% confidence) (UNUSED)
- Line 329: unused method 'refresh_screen' (60% confidence) (UNUSED)

#### pretty.py
- Line 945: unused variable 'price' (60% confidence) (UNUSED)
- Line 947: unused variable 'reviews' (60% confidence) (UNUSED)

#### progress.py
- Line 503: unused attribute '_update_time' (60% confidence) (UNUSED)
- Line 537: unused class 'RenderableColumn' (60% confidence) (UNUSED)
- Line 580: unused method 'set_spinner' (60% confidence) (UNUSED)
- Line 818: unused class 'TotalFileSizeColumn' (60% confidence) (UNUSED)
- Line 827: unused class 'MofNCompleteColumn' (60% confidence) (UNUSED)
- Line 1143: unused property 'task_ids' (60% confidence) (UNUSED)
- Line 1386: unused method 'stop_task' (60% confidence) (UNUSED)
- Line 1627: unused method 'remove_task' (60% confidence) (UNUSED)
- Line 1695: unused variable 'task3' (60% confidence) (UNUSED)

#### progress_bar.py
- Line 55: unused attribute '_pulse_segments' (60% confidence) (UNUSED)
- Line 60: unused property 'percentage_completed' (60% confidence) (UNUSED)

#### prompt.py
- Line 310: unused class 'FloatPrompt' (60% confidence) (UNUSED)

#### scope.py
- Line 76: unused variable 'list_of_things' (60% confidence) (UNUSED)
- Line 77: unused variable 'dict_of_things' (60% confidence) (UNUSED)

#### segment.py
- Line 683: unused class 'SegmentLines' (60% confidence) (UNUSED)

#### style.py
- Line 280: unused property 'link_id' (60% confidence) (UNUSED)
- Line 648: unused method 'clear_meta_and_links' (60% confidence) (UNUSED)

#### terminal_theme.py
- Line 57: unused variable 'MONOKAI' (60% confidence) (UNUSED)
- Line 81: unused variable 'DIMMED_MONOKAI' (60% confidence) (UNUSED)
- Line 105: unused variable 'NIGHT_OWLISH' (60% confidence) (UNUSED)

#### traceback.py
- Line 156: unused attribute '_showtraceback' (60% confidence) (UNUSED)
- Line 159: unused attribute 'showsyntaxerror' (60% confidence) (UNUSED)

#### six.py
- Line 43: unused variable 'class_types' (60% confidence) (UNUSED)
- Line 47: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 51: unused variable 'class_types' (60% confidence) (UNUSED)
- Line 57: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 68: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 71: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 236: unused method 'create_module' (60% confidence) (UNUSED)
- Line 501: unused variable 'robotparser' (60% confidence) (UNUSED)
- Line 510: unused function 'add_move' (60% confidence) (UNUSED)
- Line 515: unused function 'remove_move' (60% confidence) (UNUSED)
- Line 563: unused variable 'create_bound_method' (60% confidence) (UNUSED)
- Line 565: unused function 'create_unbound_method' (60% confidence) (UNUSED)
- Line 573: unused function 'create_bound_method' (60% confidence) (UNUSED)
- Line 576: unused function 'create_unbound_method' (60% confidence) (UNUSED)
- Line 589: unused variable 'get_method_function' (60% confidence) (UNUSED)
- Line 590: unused variable 'get_method_self' (60% confidence) (UNUSED)
- Line 591: unused variable 'get_function_closure' (60% confidence) (UNUSED)
- Line 592: unused variable 'get_function_code' (60% confidence) (UNUSED)
- Line 593: unused variable 'get_function_defaults' (60% confidence) (UNUSED)
- Line 594: unused variable 'get_function_globals' (60% confidence) (UNUSED)
- Line 610: unused variable 'viewkeys' (60% confidence) (UNUSED)
- Line 612: unused variable 'viewvalues' (60% confidence) (UNUSED)
- Line 614: unused variable 'viewitems' (60% confidence) (UNUSED)
- Line 628: unused variable 'viewkeys' (60% confidence) (UNUSED)
- Line 630: unused variable 'viewvalues' (60% confidence) (UNUSED)
- Line 632: unused variable 'viewitems' (60% confidence) (UNUSED)
- Line 650: unused variable 'int2byte' (60% confidence) (UNUSED)
- Line 652: unused variable 'byte2int' (60% confidence) (UNUSED)
- Line 653: unused variable 'indexbytes' (60% confidence) (UNUSED)
- Line 654: unused variable 'iterbytes' (60% confidence) (UNUSED)
- Line 676: unused variable 'int2byte' (60% confidence) (UNUSED)
- Line 678: unused function 'byte2int' (60% confidence) (UNUSED)
- Line 681: unused function 'indexbytes' (60% confidence) (UNUSED)
- Line 683: unused variable 'iterbytes' (60% confidence) (UNUSED)
- Line 694: unused method 'assertCountEqual' (60% confidence) (UNUSED)
- Line 706: unused method 'assertNotRegex' (60% confidence) (UNUSED)
- Line 753: unused variable 'from_value' (100% confidence) (UNUSED)
- Line 856: unused function 'with_metaclass' (60% confidence) (UNUSED)
- Line 863: unused variable 'this_bases' (100% confidence) (UNUSED)
- Line 875: unused variable 'this_bases' (100% confidence) (UNUSED)
- Line 958: unused function 'python_2_unicode_compatible' (60% confidence) (UNUSED)

#### stop.py
- Line 41: unused variable 'StopBaseT' (60% confidence) (UNUSED)

#### wait.py
- Line 44: unused variable 'WaitBaseT' (60% confidence) (UNUSED)

#### _api.py
- Line 80: unused attribute 'sslobject_class' (60% confidence) (UNUSED)
- Line 168: unused method 'cert_store_stats' (60% confidence) (UNUSED)

#### _macos.py
- Line 81: unused variable 'SecTrustOptionFlags' (60% confidence) (UNUSED)
- Line 270: unused variable 'errSecIncompleteCertRevocationCheck' (60% confidence) (UNUSED)
- Line 490: unused attribute 'verify_message' (60% confidence) (UNUSED)
- Line 491: unused attribute 'verify_code' (60% confidence) (UNUSED)

#### _windows.py
- Line 202: unused variable 'USAGE_MATCH_TYPE_OR' (60% confidence) (UNUSED)
- Line 350: unused attribute 'cUsageIdentifier' (60% confidence) (UNUSED)
- Line 351: unused attribute 'rgpszUsageIdentifier' (60% confidence) (UNUSED)
- Line 355: unused attribute 'RequestedUsage' (60% confidence) (UNUSED)
- Line 356: unused attribute 'cbSize' (60% confidence) (UNUSED)
- Line 431: unused attribute 'cbSize' (60% confidence) (UNUSED)
- Line 434: unused attribute 'dwAuthType' (60% confidence) (UNUSED)
- Line 435: unused attribute 'fdwChecks' (60% confidence) (UNUSED)
- Line 437: unused attribute 'pwszServerName' (60% confidence) (UNUSED)
- Line 440: unused attribute 'pvExtraPolicyPara' (60% confidence) (UNUSED)
- Line 444: unused attribute 'dwFlags' (60% confidence) (UNUSED)
- Line 446: unused attribute 'dwFlags' (60% confidence) (UNUSED)
- Line 447: unused attribute 'cbSize' (60% confidence) (UNUSED)
- Line 451: unused attribute 'cbSize' (60% confidence) (UNUSED)
- Line 484: unused attribute 'verify_message' (60% confidence) (UNUSED)
- Line 485: unused attribute 'verify_code' (60% confidence) (UNUSED)
- Line 518: unused attribute 'cbSize' (60% confidence) (UNUSED)
- Line 519: unused attribute 'hExclusiveRoot' (60% confidence) (UNUSED)

#### typing_extensions.py
- Line 966: unused attribute '__mro_entries__' (60% confidence) (UNUSED)
- Line 1064: unused attribute '__optional_keys__' (60% confidence) (UNUSED)
- Line 1189: unused variable '__typ' (100% confidence) (UNUSED)
- Line 2434: unused attribute '__dataclass_transform__' (60% confidence) (UNUSED)
- Line 2478: unused attribute '__override__' (60% confidence) (UNUSED)
- Line 2605: unused attribute '_field_types' (60% confidence) (UNUSED)

#### _collections.py
- Line 273: unused variable 'getallmatchingheaders' (60% confidence) (UNUSED)

#### connection.py
- Line 554: unused attribute '_peer_cert' (60% confidence) (UNUSED)

#### connectionpool.py
- Line 218: unused attribute 'num_requests' (60% confidence) (UNUSED)
- Line 395: unused attribute 'num_requests' (60% confidence) (UNUSED)

#### bindings.py
- Line 129: unused variable 'SecTrustOptionFlags' (60% confidence) (UNUSED)
- Line 270: unused attribute 'argstypes' (60% confidence) (UNUSED)
- Line 320: unused attribute 'kSecImportExportPassphrase' (60% confidence) (UNUSED)
- Line 323: unused attribute 'kSecImportItemIdentity' (60% confidence) (UNUSED)
- Line 446: unused variable 'kTLSProtocolMaxSupported' (60% confidence) (UNUSED)
- Line 451: unused variable 'kSecFormatPEMSequence' (60% confidence) (UNUSED)
- Line 453: unused variable 'kSecTrustResultInvalid' (60% confidence) (UNUSED)
- Line 457: unused variable 'kSecTrustResultDeny' (60% confidence) (UNUSED)
- Line 459: unused variable 'kSecTrustResultRecoverableTrustFailure' (60% confidence) (UNUSED)
- Line 460: unused variable 'kSecTrustResultFatalTrustFailure' (60% confidence) (UNUSED)
- Line 461: unused variable 'kSecTrustResultOtherError' (60% confidence) (UNUSED)
- Line 463: unused variable 'errSSLProtocol' (60% confidence) (UNUSED)
- Line 469: unused variable 'errSSLXCertChainInvalid' (60% confidence) (UNUSED)
- Line 470: unused variable 'errSSLCrypto' (60% confidence) (UNUSED)
- Line 472: unused variable 'errSSLCertExpired' (60% confidence) (UNUSED)
- Line 473: unused variable 'errSSLCertNotYetValid' (60% confidence) (UNUSED)
- Line 474: unused variable 'errSSLUnknownRootCert' (60% confidence) (UNUSED)
- Line 475: unused variable 'errSSLNoRootCert' (60% confidence) (UNUSED)
- Line 476: unused variable 'errSSLHostNameMismatch' (60% confidence) (UNUSED)
- Line 477: unused variable 'errSSLPeerHandshakeFail' (60% confidence) (UNUSED)
- Line 478: unused variable 'errSSLPeerUserCancelled' (60% confidence) (UNUSED)
- Line 479: unused variable 'errSSLWeakPeerEphemeralDHKey' (60% confidence) (UNUSED)
- Line 481: unused variable 'errSSLRecordOverflow' (60% confidence) (UNUSED)
- Line 483: unused variable 'errSecVerifyFailed' (60% confidence) (UNUSED)
- Line 484: unused variable 'errSecNoTrustSettings' (60% confidence) (UNUSED)
- Line 485: unused variable 'errSecItemNotFound' (60% confidence) (UNUSED)
- Line 486: unused variable 'errSecInvalidTrustSettings' (60% confidence) (UNUSED)

#### low_level.py
- Line 37: unused function '_cf_dictionary_from_tuples' (60% confidence) (UNUSED)

#### appengine.py
- Line 79: unused class 'AppEngineManager' (60% confidence) (UNUSED)

#### pyopenssl.py
- Line 401: unused method '_reuse' (60% confidence) (UNUSED)
- Line 404: unused method '_drop' (60% confidence) (UNUSED)
- Line 517: unused variable 'err_depth' (100% confidence) (UNUSED)

#### securetransport.py
- Line 483: unused variable 'client_key_passphrase' (100% confidence) (UNUSED)
- Line 757: unused method '_reuse' (60% confidence) (UNUSED)
- Line 760: unused method '_drop' (60% confidence) (UNUSED)
- Line 876: unused attribute '_client_cert_passphrase' (60% confidence) (UNUSED)

#### fields.py
- Line 24: unused function 'format_header_param_rfc2231' (60% confidence) (UNUSED)
- Line 123: unused variable 'format_header_param' (60% confidence) (UNUSED)

#### six.py
- Line 43: unused variable 'class_types' (60% confidence) (UNUSED)
- Line 47: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 51: unused variable 'class_types' (60% confidence) (UNUSED)
- Line 57: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 68: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 71: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 233: unused method 'create_module' (60% confidence) (UNUSED)
- Line 533: unused variable 'robotparser' (60% confidence) (UNUSED)
- Line 544: unused function 'add_move' (60% confidence) (UNUSED)
- Line 549: unused function 'remove_move' (60% confidence) (UNUSED)
- Line 602: unused variable 'create_bound_method' (60% confidence) (UNUSED)
- Line 604: unused function 'create_unbound_method' (60% confidence) (UNUSED)
- Line 613: unused function 'create_bound_method' (60% confidence) (UNUSED)
- Line 616: unused function 'create_unbound_method' (60% confidence) (UNUSED)
- Line 629: unused variable 'get_method_function' (60% confidence) (UNUSED)
- Line 630: unused variable 'get_method_self' (60% confidence) (UNUSED)
- Line 631: unused variable 'get_function_closure' (60% confidence) (UNUSED)
- Line 632: unused variable 'get_function_code' (60% confidence) (UNUSED)
- Line 633: unused variable 'get_function_defaults' (60% confidence) (UNUSED)
- Line 634: unused variable 'get_function_globals' (60% confidence) (UNUSED)
- Line 651: unused variable 'viewkeys' (60% confidence) (UNUSED)
- Line 653: unused variable 'viewvalues' (60% confidence) (UNUSED)
- Line 655: unused variable 'viewitems' (60% confidence) (UNUSED)
- Line 670: unused variable 'viewkeys' (60% confidence) (UNUSED)
- Line 672: unused variable 'viewvalues' (60% confidence) (UNUSED)
- Line 674: unused variable 'viewitems' (60% confidence) (UNUSED)
- Line 695: unused variable 'int2byte' (60% confidence) (UNUSED)
- Line 697: unused variable 'byte2int' (60% confidence) (UNUSED)
- Line 698: unused variable 'indexbytes' (60% confidence) (UNUSED)
- Line 699: unused variable 'iterbytes' (60% confidence) (UNUSED)
- Line 725: unused variable 'int2byte' (60% confidence) (UNUSED)
- Line 727: unused function 'byte2int' (60% confidence) (UNUSED)
- Line 730: unused function 'indexbytes' (60% confidence) (UNUSED)
- Line 733: unused variable 'iterbytes' (60% confidence) (UNUSED)
- Line 745: unused method 'assertCountEqual' (60% confidence) (UNUSED)
- Line 757: unused method 'assertNotRegex' (60% confidence) (UNUSED)
- Line 810: unused variable 'from_value' (100% confidence) (UNUSED)
- Line 929: unused function 'with_metaclass' (60% confidence) (UNUSED)
- Line 935: unused variable 'this_bases' (100% confidence) (UNUSED)
- Line 947: unused variable 'this_bases' (100% confidence) (UNUSED)
- Line 1033: unused function 'python_2_unicode_compatible' (60% confidence) (UNUSED)

#### queue.py
- Line 15: unused method '_qsize' (60% confidence) (UNUSED)

#### url.py
- Line 61: unused variable 'IPV6_RE' (60% confidence) (UNUSED)

#### __init__.py
- Line 96: unused variable 'resources_stream' (60% confidence) (UNUSED)
- Line 98: unused variable 'resource_dir' (60% confidence) (UNUSED)
- Line 154: unused function '_sget_dict' (60% confidence) (UNUSED)
- Line 158: unused function '_sset_dict' (60% confidence) (UNUSED)
- Line 163: unused function '_sget_object' (60% confidence) (UNUSED)
- Line 167: unused function '_sset_object' (60% confidence) (UNUSED)
- Line 314: unused property 'requirers_str' (60% confidence) (UNUSED)
- Line 2671: unused method '_warn_legacy_version' (60% confidence) (UNUSED)
- Line 3022: unused variable 'EQEQ' (60% confidence) (UNUSED)
- Line 3095: unused class 'RequirementParseError' (60% confidence) (UNUSED)
- Line 3259: unused function '_initialize_master_working_set' (60% confidence) (UNUSED)

#### appdirs.py
- Line 560: unused import 'win32com' (90% confidence) (UNUSED)

#### abc.py
- Line 22: unused method 'resource_path' (60% confidence) (UNUSED)
- Line 130: unused method 'resource_path' (60% confidence) (UNUSED)

#### readers.py
- Line 19: unused method 'resource_path' (60% confidence) (UNUSED)
- Line 113: unused method 'resource_path' (60% confidence) (UNUSED)

#### simple.py
- Line 108: unused class 'TraversableReader' (60% confidence) (UNUSED)

#### context.py
- Line 20: unused function 'tarball_context' (60% confidence) (UNUSED)
- Line 72: unused function 'repo_context' (60% confidence) (UNUSED)

#### functools.py
- Line 40: unused function 'method_caller' (60% confidence) (UNUSED)
- Line 241: unused function 'result_invoke' (60% confidence) (UNUSED)
- Line 269: unused function 'call_aside' (60% confidence) (UNUSED)
- Line 341: unused variable 'attempt' (60% confidence) (UNUSED)
- Line 376: unused function 'print_yielded' (60% confidence) (UNUSED)
- Line 410: unused function 'assign_params' (60% confidence) (UNUSED)
- Line 442: unused function 'save_method_args' (60% confidence) (UNUSED)
- Line 488: unused function 'except_' (60% confidence) (UNUSED)

#### __init__.py
- Line 22: unused function 'multi_substitution' (60% confidence) (UNUSED)
- Line 317: unused method 'headless_camel_case' (60% confidence) (UNUSED)
- Line 323: unused method 'underscore_separated' (60% confidence) (UNUSED)
- Line 326: unused method 'dash_separated' (60% confidence) (UNUSED)
- Line 329: unused method 'space_separated' (60% confidence) (UNUSED)
- Line 376: unused method 'from_class_name' (60% confidence) (UNUSED)
- Line 385: unused function 'simple_html_strip' (60% confidence) (UNUSED)
- Line 407: unused class 'SeparatedValues' (60% confidence) (UNUSED)
- Line 428: unused class 'Stripper' (60% confidence) (UNUSED)
- Line 510: unused function 'normalize_newlines' (60% confidence) (UNUSED)

#### more.py
- Line 3274: unused attribute 'timed_out' (60% confidence) (UNUSED)
- Line 3282: unused attribute 'timed_out' (60% confidence) (UNUSED)
- Line 4017: unused attribute 'items_seen' (60% confidence) (UNUSED)
- Line 4024: unused attribute 'items_seen' (60% confidence) (UNUSED)
- Line 4073: unused variable 'num_partial' (60% confidence) (UNUSED)
- Line 4094: unused variable 'num_partial' (60% confidence) (UNUSED)

#### _manylinux.py
- Line 28: unused variable 'EM_S390' (60% confidence) (UNUSED)
- Line 30: unused variable 'EM_X86_64' (60% confidence) (UNUSED)
- Line 53: unused attribute 'e_ident_version' (60% confidence) (UNUSED)
- Line 54: unused attribute 'e_ident_osabi' (60% confidence) (UNUSED)
- Line 55: unused attribute 'e_ident_abiversion' (60% confidence) (UNUSED)
- Line 56: unused attribute 'e_ident_pad' (60% confidence) (UNUSED)
- Line 61: unused attribute 'e_type' (60% confidence) (UNUSED)
- Line 63: unused attribute 'e_version' (60% confidence) (UNUSED)
- Line 64: unused attribute 'e_entry' (60% confidence) (UNUSED)
- Line 66: unused attribute 'e_shoff' (60% confidence) (UNUSED)
- Line 68: unused attribute 'e_ehsize' (60% confidence) (UNUSED)
- Line 71: unused attribute 'e_shentsize' (60% confidence) (UNUSED)
- Line 72: unused attribute 'e_shnum' (60% confidence) (UNUSED)
- Line 73: unused attribute 'e_shstrndx' (60% confidence) (UNUSED)

#### specifiers.py
- Line 269: unused method '_compare_not_equal' (60% confidence) (UNUSED)
- Line 272: unused method '_compare_less_than_equal' (60% confidence) (UNUSED)
- Line 275: unused method '_compare_greater_than_equal' (60% confidence) (UNUSED)
- Line 280: unused method '_compare_less_than' (60% confidence) (UNUSED)
- Line 283: unused method '_compare_greater_than' (60% confidence) (UNUSED)
- Line 407: unused method '_compare_compatible' (60% confidence) (UNUSED)
- Line 469: unused method '_compare_not_equal' (60% confidence) (UNUSED)
- Line 473: unused method '_compare_less_than_equal' (60% confidence) (UNUSED)
- Line 481: unused method '_compare_greater_than_equal' (60% confidence) (UNUSED)
- Line 491: unused method '_compare_less_than' (60% confidence) (UNUSED)
- Line 517: unused method '_compare_greater_than' (60% confidence) (UNUSED)
- Line 549: unused method '_compare_arbitrary' (60% confidence) (UNUSED)

#### version.py
- Line 33: unused variable 'VersionComparisonMethod' (60% confidence) (UNUSED)
- Line 163: unused property 'is_devrelease' (60% confidence) (UNUSED)
- Line 376: unused property 'is_devrelease' (60% confidence) (UNUSED)

#### __init__.py
- Line 162: unused variable 'core_builtin_exprs' (60% confidence) (UNUSED)

#### common.py
- Line 167: unused variable 'hex_integer' (60% confidence) (UNUSED)
- Line 212: unused variable 'fnumber' (60% confidence) (UNUSED)
- Line 240: unused variable 'ipv6_address' (60% confidence) (UNUSED)
- Line 247: unused variable 'mac_address' (60% confidence) (UNUSED)
- Line 306: unused variable 'iso8601_date' (60% confidence) (UNUSED)
- Line 311: unused variable 'iso8601_datetime' (60% confidence) (UNUSED)
- Line 413: unused variable 'convertToInteger' (60% confidence) (UNUSED)
- Line 414: unused variable 'convertToFloat' (60% confidence) (UNUSED)
- Line 415: unused variable 'convertToDate' (60% confidence) (UNUSED)
- Line 416: unused variable 'convertToDatetime' (60% confidence) (UNUSED)
- Line 417: unused variable 'stripHTMLTags' (60% confidence) (UNUSED)
- Line 418: unused variable 'upcaseTokens' (60% confidence) (UNUSED)
- Line 419: unused variable 'downcaseTokens' (60% confidence) (UNUSED)

#### core.py
- Line 167: unused function 'enable_diag' (60% confidence) (UNUSED)
- Line 174: unused function 'disable_diag' (60% confidence) (UNUSED)
- Line 197: unused variable 'w_line' (60% confidence) (UNUSED)
- Line 779: unused variable 'MATCH' (60% confidence) (UNUSED)
- Line 913: unused variable 'MATCH' (60% confidence) (UNUSED)
- Line 2145: unused method 'create_diagram' (60% confidence) (UNUSED)
- Line 2191: unused variable 'setDefaultWhitespaceChars' (60% confidence) (UNUSED)
- Line 2193: unused variable 'setResultsName' (60% confidence) (UNUSED)
- Line 2194: unused variable 'setBreak' (60% confidence) (UNUSED)
- Line 2196: unused variable 'addParseAction' (60% confidence) (UNUSED)
- Line 2197: unused variable 'addCondition' (60% confidence) (UNUSED)
- Line 2198: unused variable 'setFailAction' (60% confidence) (UNUSED)
- Line 2202: unused variable 'enableLeftRecursion' (60% confidence) (UNUSED)
- Line 2203: unused variable 'enablePackrat' (60% confidence) (UNUSED)
- Line 2205: unused variable 'scanString' (60% confidence) (UNUSED)
- Line 2206: unused variable 'searchString' (60% confidence) (UNUSED)
- Line 2207: unused variable 'transformString' (60% confidence) (UNUSED)
- Line 2208: unused variable 'setWhitespaceChars' (60% confidence) (UNUSED)
- Line 2209: unused variable 'parseWithTabs' (60% confidence) (UNUSED)
- Line 2210: unused variable 'setDebugActions' (60% confidence) (UNUSED)
- Line 2211: unused variable 'setDebug' (60% confidence) (UNUSED)
- Line 2214: unused variable 'parseFile' (60% confidence) (UNUSED)
- Line 2215: unused variable 'runTests' (60% confidence) (UNUSED)
- Line 2216: unused variable 'ignoreWhitespace' (60% confidence) (UNUSED)
- Line 2469: unused variable 'setDefaultKeywordChars' (60% confidence) (UNUSED)
- Line 2715: unused attribute 'bodyCharsOrig' (60% confidence) (UNUSED)
- Line 2718: unused attribute 'bodyCharsOrig' (60% confidence) (UNUSED)
- Line 3753: unused variable 'ignoreWhitespace' (60% confidence) (UNUSED)
- Line 4433: unused variable 'ignoreWhitespace' (60% confidence) (UNUSED)
- Line 5359: unused variable 'ignoreWhitespace' (60% confidence) (UNUSED)

#### __init__.py
- Line 313: unused attribute 'extracted_diagram_names' (60% confidence) (UNUSED)
- Line 327: unused method 'generate_unnamed' (60% confidence) (UNUSED)

#### exceptions.py
- Line 217: unused variable 'markInputline' (60% confidence) (UNUSED)

#### helpers.py
- Line 644: unused attribute 'tag_body' (60% confidence) (UNUSED)

#### results.py
- Line 162: unused attribute '_modal' (60% confidence) (UNUSED)
- Line 755: unused variable 'asDict' (60% confidence) (UNUSED)

#### testing.py
- Line 20: unused class 'reset_pyparsing_context' (60% confidence) (UNUSED)
- Line 141: unused method 'assertParseAndCheckList' (60% confidence) (UNUSED)
- Line 155: unused method 'assertParseAndCheckDict' (60% confidence) (UNUSED)
- Line 169: unused method 'assertRunTestResults' (60% confidence) (UNUSED)
- Line 232: unused method 'assertRaisesParseException' (60% confidence) (UNUSED)

#### unicode.py
- Line 290: unused class 'CJK' (60% confidence) (UNUSED)
- Line 338: unused attribute 'BMP' (60% confidence) (UNUSED)
- Line 341: unused attribute 'العربية' (60% confidence) (UNUSED)
- Line 342: unused attribute '中文' (60% confidence) (UNUSED)
- Line 343: unused attribute 'кириллица' (60% confidence) (UNUSED)
- Line 344: unused attribute 'Ελληνικά' (60% confidence) (UNUSED)
- Line 345: unused attribute 'עִברִית' (60% confidence) (UNUSED)
- Line 346: unused attribute '日本語' (60% confidence) (UNUSED)
- Line 347: unused attribute '漢字' (60% confidence) (UNUSED)
- Line 348: unused attribute 'カタカナ' (60% confidence) (UNUSED)
- Line 349: unused attribute 'ひらがな' (60% confidence) (UNUSED)
- Line 350: unused attribute '한국어' (60% confidence) (UNUSED)
- Line 351: unused attribute 'ไทย' (60% confidence) (UNUSED)
- Line 352: unused attribute 'देवनागरी' (60% confidence) (UNUSED)

#### __init__.py
- Line 51: unused method 'create_module' (60% confidence) (UNUSED)

#### api.py
- Line 281: unused method 'iter_config_paths' (60% confidence) (UNUSED)
- Line 286: unused method 'iter_data_paths' (60% confidence) (UNUSED)
- Line 291: unused method 'iter_cache_paths' (60% confidence) (UNUSED)
- Line 296: unused method 'iter_runtime_paths' (60% confidence) (UNUSED)

#### __init__.py
- Line 112: unused function 'show_info' (60% confidence) (UNUSED)
- Line 342: unused function 'create_library_symlinks' (60% confidence) (UNUSED)
- Line 400: unused variable 'pkg_config_executable' (60% confidence) (UNUSED)

#### acero.py
- Line 259: unused function '_perform_join_asof' (60% confidence) (UNUSED)
- Line 382: unused function '_sort_source' (60% confidence) (UNUSED)
- Line 404: unused function '_group_by' (60% confidence) (UNUSED)

#### benchmark.py
- Line 21: unused import 'benchmark_PandasObjectIsNull' (90% confidence) (UNUSED)

#### compute.py
- Line 307: unused attribute '__signature__' (60% confidence) (UNUSED)

#### conftest.py
- Line 220: unused function 'pytest_ignore_collect' (60% confidence) (UNUSED)
- Line 268: unused function '_docdir' (60% confidence) (UNUSED)
- Line 289: unused function 'add_fs' (60% confidence) (UNUSED)
- Line 333: unused function 'unary_agg_func_fixture' (60% confidence) (UNUSED)
- Line 359: unused function 'varargs_agg_func_fixture' (60% confidence) (UNUSED)

#### fs.py
- Line 39: unused variable 'FileStats' (60% confidence) (UNUSED)
- Line 296: unused method 'get_type_name' (60% confidence) (UNUSED)
- Line 329: unused method 'get_file_info_selector' (60% confidence) (UNUSED)
- Line 387: unused method 'delete_root_dir_contents' (60% confidence) (UNUSED)

#### buffer.py
- Line 29: unused variable 'CPU_PINNED' (60% confidence) (UNUSED)
- Line 30: unused variable 'OPENCL' (60% confidence) (UNUSED)
- Line 31: unused variable 'VULKAN' (60% confidence) (UNUSED)
- Line 32: unused variable 'METAL' (60% confidence) (UNUSED)
- Line 33: unused variable 'VPI' (60% confidence) (UNUSED)
- Line 34: unused variable 'ROCM' (60% confidence) (UNUSED)

#### column.py
- Line 136: unused variable 'is_ordered' (60% confidence) (UNUSED)
- Line 148: unused variable 'LITTLE' (60% confidence) (UNUSED)
- Line 149: unused variable 'BIG' (60% confidence) (UNUSED)

#### pandas_compat.py
- Line 551: unused function 'dataframe_to_types' (60% confidence) (UNUSED)
- Line 586: unused function 'dataframe_to_arrays' (60% confidence) (UNUSED)
- Line 782: unused function 'table_to_dataframe' (60% confidence) (UNUSED)
- Line 1270: unused function 'make_tz_aware' (60% confidence) (UNUSED)

#### core.py
- Line 977: unused variable 'writer_engine_version' (100% confidence) (UNUSED)
- Line 1148: unused variable 'EXCLUDED_PARQUET_PATHS' (60% confidence) (UNUSED)

#### conftest.py
- Line 74: unused function 'pytest_addoption' (60% confidence) (UNUSED)
- Line 113: unused function 'pytest_configure' (60% confidence) (UNUSED)
- Line 130: unused function 'pytest_runtest_setup' (60% confidence) (UNUSED)
- Line 147: unused function 'disable_aws_metadata' (60% confidence) (UNUSED)
- Line 320: unused function 'builtin_pickle' (60% confidence) (UNUSED)
- Line 326: unused function 'cloudpickle' (60% confidence) (UNUSED)

#### encryption.py
- Line 32: unused method 'wrap_key' (60% confidence) (UNUSED)
- Line 41: unused method 'unwrap_key' (60% confidence) (UNUSED)

#### test_encryption.py
- Line 284: unused method 'wrap_key' (60% confidence) (UNUSED)
- Line 287: unused method 'unwrap_key' (60% confidence) (UNUSED)
- Line 338: unused method 'wrap_key' (60% confidence) (UNUSED)
- Line 341: unused method 'unwrap_key' (60% confidence) (UNUSED)

#### strategies.py
- Line 95: unused variable 'decimal32_type' (60% confidence) (UNUSED)
- Line 100: unused variable 'decimal64_type' (60% confidence) (UNUSED)

#### test_cffi.py
- Line 489: unreachable 'else' block (100% confidence) (UNUSED)

#### test_compute.py
- Line 46: unused import 'pas' (90% confidence) (UNUSED)
- Line 48: unused variable 'pas' (60% confidence) (UNUSED)
- Line 2031: unused attribute 'rounding' (60% confidence) (UNUSED)

#### test_convert_builtin.py
- Line 48: unused variable 'np_str_int_types' (60% confidence) (UNUSED)

#### test_csv.py
- Line 107: unused attribute 'zzz_non_existent' (60% confidence) (UNUSED)
- Line 212: unused attribute 'autogenerate_column_names' (60% confidence) (UNUSED)
- Line 268: unused attribute 'escape_char' (60% confidence) (UNUSED)
- Line 273: unused attribute 'escape_char' (60% confidence) (UNUSED)
- Line 303: unused attribute 'decimal_point' (60% confidence) (UNUSED)
- Line 842: unused attribute 'autogenerate_column_names' (60% confidence) (UNUSED)
- Line 867: unused attribute 'include_columns' (60% confidence) (UNUSED)
- Line 875: unused attribute 'include_columns' (60% confidence) (UNUSED)
- Line 886: unused attribute 'include_columns' (60% confidence) (UNUSED)
- Line 897: unused attribute 'include_columns' (60% confidence) (UNUSED)
- Line 898: unused attribute 'include_missing_columns' (60% confidence) (UNUSED)
- Line 913: unused attribute 'include_columns' (60% confidence) (UNUSED)
- Line 1156: unused attribute 'check_utf8' (60% confidence) (UNUSED)
- Line 1167: unused attribute 'check_utf8' (60% confidence) (UNUSED)
- Line 1204: unused attribute 'quoted_strings_can_be_null' (60% confidence) (UNUSED)
- Line 1689: unused attribute 'include_columns' (60% confidence) (UNUSED)
- Line 1709: unused attribute 'include_columns' (60% confidence) (UNUSED)
- Line 1716: unused attribute 'include_missing_columns' (60% confidence) (UNUSED)

#### test_cuda_numba_interop.py
- Line 106: unsatisfiable 'if' condition (100% confidence) (UNUSED)

#### test_dataset_encryption.py
- Line 180: unused method 'wrap_key' (60% confidence) (UNUSED)
- Line 184: unused method 'unwrap_key' (60% confidence) (UNUSED)

#### test_extension_type.py
- Line 102: unused variable 'maps_as_pydicts' (100% confidence) (UNUSED)

#### test_flight.py
- Line 595: unused method 'start_call' (60% confidence) (UNUSED)
- Line 621: unused method 'received_headers' (60% confidence) (UNUSED)
- Line 631: unused method 'start_call' (60% confidence) (UNUSED)
- Line 683: unused method 'start_call' (60% confidence) (UNUSED)
- Line 728: unused method 'start_call' (60% confidence) (UNUSED)
- Line 754: unused method 'start_call' (60% confidence) (UNUSED)
- Line 771: unused method 'start_call' (60% confidence) (UNUSED)
- Line 789: unused method 'start_call' (60% confidence) (UNUSED)
- Line 801: unused method 'start_call' (60% confidence) (UNUSED)
- Line 814: unused method 'start_call' (60% confidence) (UNUSED)
- Line 835: unused method 'received_headers' (60% confidence) (UNUSED)
- Line 844: unused method 'start_call' (60% confidence) (UNUSED)
- Line 1451: unused variable 'header_auth_server_middleware_factory' (60% confidence) (UNUSED)
- Line 2499: unused method 'start_call' (60% confidence) (UNUSED)
- Line 2506: unused method 'received_headers' (60% confidence) (UNUSED)

#### test_fs.py
- Line 60: unused method 'get_type_name' (60% confidence) (UNUSED)
- Line 82: unused method 'get_file_info_selector' (60% confidence) (UNUSED)
- Line 114: unused method 'delete_root_dir_contents' (60% confidence) (UNUSED)
- Line 161: unused function 'py_localfs' (60% confidence) (UNUSED)
- Line 191: unused function 'localfs_with_mmap' (60% confidence) (UNUSED)
- Line 201: unused function 'subtree_localfs' (60% confidence) (UNUSED)
- Line 211: unused function 'gcsfs' (60% confidence) (UNUSED)
- Line 268: unused function 'subtree_s3fs' (60% confidence) (UNUSED)
- Line 301: unused function 'azurefs' (60% confidence) (UNUSED)
- Line 349: unused function 'py_fsspec_localfs' (60% confidence) (UNUSED)
- Line 361: unused function 'py_fsspec_memoryfs' (60% confidence) (UNUSED)
- Line 376: unused function 'py_fsspec_s3fs' (60% confidence) (UNUSED)

#### test_ipc.py
- Line 127: unused class 'MessageFixture' (60% confidence) (UNUSED)
- Line 133: unused function 'ipc_fixture' (60% confidence) (UNUSED)
- Line 849: unused variable 'client_address' (60% confidence) (UNUSED)

#### test_jvm.py
- Line 405: unused attribute 'isSet' (60% confidence) (UNUSED)
- Line 407: unused attribute 'isSet' (60% confidence) (UNUSED)

#### test_pandas.py
- Line 3281: unused function '_fully_loaded_dataframe_example' (60% confidence) (UNUSED)
- Line 3320: unused function '_pytime_from_micros' (60% confidence) (UNUSED)
- Line 4379: unused method '_Int64Dtype__from_arrow__' (60% confidence) (UNUSED)

#### test_substrait.py
- Line 612: unused variable 'varargs_agg_func_fixture' (100% confidence) (UNUSED)
- Line 761: unused variable 'varargs_agg_func_fixture' (100% confidence) (UNUSED)

#### test_table.py
- Line 3505: unused function 'cpu_and_cuda_chunked_array' (60% confidence) (UNUSED)
- Line 3532: unused function 'cpu_and_cuda_table' (60% confidence) (UNUSED)
- Line 3538: unused variable 'cpu_and_cuda_chunked_array' (100% confidence) (UNUSED)

#### test_udf.py
- Line 50: unused function 'sum_agg_func_fixture' (60% confidence) (UNUSED)
- Line 72: unused function 'exception_agg_func_fixture' (60% confidence) (UNUSED)
- Line 76: unreachable code after 'raise' (100% confidence) (UNUSED)
- Line 92: unused function 'wrong_output_dtype_agg_func_fixture' (60% confidence) (UNUSED)
- Line 111: unused function 'wrong_output_type_agg_func_fixture' (60% confidence) (UNUSED)
- Line 756: unused variable 'unary_agg_func_fixture' (100% confidence) (UNUSED)
- Line 764: unused variable 'unary_agg_func_fixture' (100% confidence) (UNUSED)
- Line 771: unused variable 'wrong_output_dtype_agg_func_fixture' (100% confidence) (UNUSED)
- Line 777: unused variable 'wrong_output_type_agg_func_fixture' (100% confidence) (UNUSED)
- Line 784: unused variable 'varargs_agg_func_fixture' (100% confidence) (UNUSED)
- Line 796: unused variable 'exception_agg_func_fixture' (100% confidence) (UNUSED)
- Line 804: unused variable 'unary_agg_func_fixture' (100% confidence) (UNUSED)
- Line 823: unused variable 'unary_agg_func_fixture' (100% confidence) (UNUSED)
- Line 835: unused variable 'wrong_output_dtype_agg_func_fixture' (100% confidence) (UNUSED)
- Line 844: unused variable 'wrong_output_type_agg_func_fixture' (100% confidence) (UNUSED)
- Line 854: unused variable 'exception_agg_func_fixture' (100% confidence) (UNUSED)
- Line 864: unused variable 'sum_agg_func_fixture' (100% confidence) (UNUSED)

#### test_util.py
- Line 34: unused variable 'whatever' (100% confidence) (UNUSED)
- Line 57: unused variable 'whatever' (100% confidence) (UNUSED)
- Line 66: unused variable 'whatever' (100% confidence) (UNUSED)
- Line 78: unused variable 'whatever' (100% confidence) (UNUSED)
- Line 83: unused variable 'whatever' (100% confidence) (UNUSED)
- Line 88: unused variable 'whatever' (100% confidence) (UNUSED)

#### util.py
- Line 43: unused function 'randsign' (60% confidence) (UNUSED)
- Line 266: unused method 'get_type_name' (60% confidence) (UNUSED)
- Line 275: unused method 'get_file_info_selector' (60% confidence) (UNUSED)
- Line 288: unused method 'delete_root_dir_contents' (60% confidence) (UNUSED)

#### types.py
- Line 243: unused function 'is_large_unicode' (60% confidence) (UNUSED)

#### util.py
- Line 109: unused function '_deprecate_class' (60% confidence) (UNUSED)
- Line 110: unused variable 'instancecheck' (100% confidence) (UNUSED)
- Line 161: unused function 'get_contiguous_span' (60% confidence) (UNUSED)

#### docscrape.py
- Line 632: unused attribute '_mod' (60% confidence) (UNUSED)
- Line 696: unused function 'get_doc_object' (60% confidence) (UNUSED)

#### version.py
- Line 206: unused property 'is_devrelease' (60% confidence) (UNUSED)
- Line 424: unused property 'is_devrelease' (60% confidence) (UNUSED)

#### _config.py
- Line 44: unused variable 'str_to_lower' (60% confidence) (UNUSED)
- Line 45: unused variable 'str_to_upper' (60% confidence) (UNUSED)
- Line 46: unused variable 'str_strip_whitespace' (60% confidence) (UNUSED)
- Line 47: unused variable 'str_min_length' (60% confidence) (UNUSED)
- Line 48: unused variable 'str_max_length' (60% confidence) (UNUSED)
- Line 58: unused variable 'loc_by_alias' (60% confidence) (UNUSED)
- Line 73: unused variable 'val_json_bytes' (60% confidence) (UNUSED)
- Line 74: unused variable 'ser_json_inf_nan' (60% confidence) (UNUSED)
- Line 79: unused variable 'hide_input_in_errors' (60% confidence) (UNUSED)
- Line 87: unused variable 'validation_error_cause' (60% confidence) (UNUSED)
- Line 89: unused variable 'cache_strings' (60% confidence) (UNUSED)
- Line 92: unused variable 'serialize_by_alias' (60% confidence) (UNUSED)

#### _core_metadata.py
- Line 40: unused variable 'pydantic_js_prefer_positional_arguments' (60% confidence) (UNUSED)
- Line 43: unused variable 'pydantic_internal_union_tag_key' (60% confidence) (UNUSED)
- Line 44: unused variable 'pydantic_internal_union_discriminator' (60% confidence) (UNUSED)

#### _core_utils.py
- Line 19: unused variable 'AnyFunctionSchema' (60% confidence) (UNUSED)

#### _dataclasses.py
- Line 148: unused attribute '__signature__' (60% confidence) (UNUSED)

#### _decorators_v1.py
- Line 116: unused variable '__values' (100% confidence) (UNUSED)
- Line 122: unused variable '__info' (100% confidence) (UNUSED)
- Line 122: unused variable '__values' (100% confidence) (UNUSED)
- Line 129: unused variable '__fields_tuple' (100% confidence) (UNUSED)
- Line 129: unused variable '__info' (100% confidence) (UNUSED)

#### _docs_extraction.py
- Line 24: unused method 'visit_AnnAssign' (60% confidence) (UNUSED)

#### _generics.py
- Line 43: unused class 'LimitedDict' (60% confidence) (UNUSED)
- Line 431: unused function 'recursively_defined_type_refs' (60% confidence) (UNUSED)

#### _known_annotated_metadata.py
- Line 41: unused variable 'SEQUENCE_CONSTRAINTS' (60% confidence) (UNUSED)
- Line 50: unused variable 'TIMEDELTA_CONSTRAINTS' (60% confidence) (UNUSED)
- Line 51: unused variable 'TIME_CONSTRAINTS' (60% confidence) (UNUSED)

#### _model_construction.py
- Line 635: unused attribute '__signature__' (60% confidence) (UNUSED)

#### _typing_extra.py
- Line 188: unused variable 'origin_is_union' (60% confidence) (UNUSED)
- Line 400: unused function 'eval_type_lenient' (60% confidence) (UNUSED)

#### color.py
- Line 156: unused method 'as_rgb' (60% confidence) (UNUSED)
- Line 192: unused method 'as_hsl' (60% confidence) (UNUSED)

#### config.py
- Line 48: unused variable 'str_to_lower' (60% confidence) (UNUSED)
- Line 51: unused variable 'str_to_upper' (60% confidence) (UNUSED)
- Line 54: unused variable 'str_strip_whitespace' (60% confidence) (UNUSED)
- Line 57: unused variable 'str_min_length' (60% confidence) (UNUSED)
- Line 60: unused variable 'str_max_length' (60% confidence) (UNUSED)
- Line 358: unused variable 'loc_by_alias' (60% confidence) (UNUSED)
- Line 611: unused variable 'val_json_bytes' (60% confidence) (UNUSED)
- Line 621: unused variable 'ser_json_inf_nan' (60% confidence) (UNUSED)
- Line 731: unused variable 'hide_input_in_errors' (60% confidence) (UNUSED)
- Line 968: unused variable 'validation_error_cause' (60% confidence) (UNUSED)
- Line 1019: unused variable 'cache_strings' (60% confidence) (UNUSED)
- Line 1114: unused variable 'serialize_by_alias' (60% confidence) (UNUSED)

#### class_validators.py
- Line 38: unused variable '__values' (100% confidence) (UNUSED)
- Line 53: unused variable 'V1RootValidator' (60% confidence) (UNUSED)

#### decorator.py
- Line 26: unused variable 'ConfigType' (60% confidence) (UNUSED)
- Line 262: unused method 'check_positional_only' (60% confidence) (UNUSED)
- Line 272: unused method 'check_duplicate_kwargs' (60% confidence) (UNUSED)

#### arguments_schema.py
- Line 14: unused function 'generate_arguments_schema' (60% confidence) (UNUSED)

#### pipeline.py
- Line 279: unused method 'not_in' (60% confidence) (UNUSED)
- Line 284: unused method 'datetime_tz_naive' (60% confidence) (UNUSED)
- Line 287: unused method 'datetime_tz_aware' (60% confidence) (UNUSED)
- Line 290: unused method 'datetime_tz' (60% confidence) (UNUSED)
- Line 295: unused method 'datetime_with_tz' (60% confidence) (UNUSED)
- Line 301: unused method 'str_lower' (60% confidence) (UNUSED)
- Line 304: unused method 'str_upper' (60% confidence) (UNUSED)
- Line 307: unused method 'str_title' (60% confidence) (UNUSED)
- Line 310: unused method 'str_strip' (60% confidence) (UNUSED)
- Line 313: unused method 'str_pattern' (60% confidence) (UNUSED)
- Line 316: unused method 'str_contains' (60% confidence) (UNUSED)
- Line 319: unused method 'str_starts_with' (60% confidence) (UNUSED)
- Line 322: unused method 'str_ends_with' (60% confidence) (UNUSED)

#### functional_serializers.py
- Line 303: unused variable 'ModelPlainSerializerWithInfo' (60% confidence) (UNUSED)
- Line 306: unused variable 'ModelPlainSerializerWithoutInfo' (60% confidence) (UNUSED)
- Line 312: unused variable 'ModelWrapSerializerWithInfo' (60% confidence) (UNUSED)
- Line 315: unused variable 'ModelWrapSerializerWithoutInfo' (60% confidence) (UNUSED)

#### functional_validators.py
- Line 528: unused variable 'outer_location' (100% confidence) (UNUSED)

#### json_schema.py
- Line 250: unused variable 'schema_dialect' (60% confidence) (UNUSED)
- Line 602: unused method 'invalid_schema' (60% confidence) (UNUSED)
- Line 898: unused method 'tuple_positional_schema' (60% confidence) (UNUSED)
- Line 909: unused method 'tuple_variable_schema' (60% confidence) (UNUSED)
- Line 1045: unused method 'function_before_schema' (60% confidence) (UNUSED)
- Line 1059: unused method 'function_after_schema' (60% confidence) (UNUSED)
- Line 1070: unused method 'function_plain_schema' (60% confidence) (UNUSED)
- Line 1086: unused method 'function_wrap_schema' (60% confidence) (UNUSED)
- Line 1100: unused method 'default_schema' (60% confidence) (UNUSED)
- Line 1429: unused method 'typed_dict_field_schema' (60% confidence) (UNUSED)
- Line 1440: unused method 'dataclass_field_schema' (60% confidence) (UNUSED)
- Line 1451: unused method 'model_field_schema' (60% confidence) (UNUSED)
- Line 1462: unused method 'computed_field_schema' (60% confidence) (UNUSED)
- Line 1966: unused method 'definition_ref_schema' (60% confidence) (UNUSED)
- Line 2416: unused function 'models_json_schema' (60% confidence) (UNUSED)
- Line 2520: unused class 'Examples' (60% confidence) (UNUSED)
- Line 2625: unused variable 'SkipJsonSchema' (60% confidence) (UNUSED)
- Line 2628: unused class 'SkipJsonSchema' (60% confidence) (UNUSED)

#### main.py
- Line 276: unused method 'model_computed_fields' (60% confidence) (UNUSED)
- Line 296: unused property 'model_fields_set' (60% confidence) (UNUSED)
- Line 748: unused method 'model_validate_strings' (60% confidence) (UNUSED)
- Line 1572: unused method 'update_forward_refs' (60% confidence) (UNUSED)

#### __init__.py
- Line 118: unused variable 'self_instance' (100% confidence) (UNUSED)
- Line 146: unused variable 'self_instance' (100% confidence) (UNUSED)

#### type_adapter.py
- Line 40: unused variable 'TypeAdapterT' (60% confidence) (UNUSED)
- Line 588: unused function 'dump_json' (60% confidence) (UNUSED)
- Line 672: unused method 'json_schemas' (60% confidence) (UNUSED)

#### types.py
- Line 2139: unused method 'human_readable' (60% confidence) (UNUSED)

#### _hypothesis_plugin.py
- Line 242: unused function 'resolve_conbytes' (60% confidence) (UNUSED)
- Line 263: unused function 'resolve_condecimal' (60% confidence) (UNUSED)
- Line 281: unused function 'resolve_confloat' (60% confidence) (UNUSED)
- Line 313: unused function 'resolve_conint' (60% confidence) (UNUSED)
- Line 336: unused function 'resolve_condate' (60% confidence) (UNUSED)
- Line 355: unused function 'resolve_constr' (60% confidence) (UNUSED)

#### class_validators.py
- Line 44: unused variable 'ValidatorsList' (60% confidence) (UNUSED)
- Line 45: unused variable 'ValidatorListDict' (60% confidence) (UNUSED)

#### color.py
- Line 119: unused method 'as_rgb' (60% confidence) (UNUSED)
- Line 153: unused method 'as_hsl' (60% confidence) (UNUSED)

#### config.py
- Line 17: unused variable 'ConfigType' (60% confidence) (UNUSED)
- Line 19: unused class 'SchemaExtraCallable' (60% confidence) (UNUSED)
- Line 25: unused variable 'model_class' (100% confidence) (UNUSED)
- Line 29: unused variable 'SchemaExtraCallable' (60% confidence) (UNUSED)

#### dataclasses.py
- Line 62: unused variable 'DataclassT' (60% confidence) (UNUSED)
- Line 64: unused variable 'DataclassClassOrWrapper' (60% confidence) (UNUSED)

#### decorator.py
- Line 17: unused variable 'ConfigType' (60% confidence) (UNUSED)
- Line 243: unused function 'check_positional_only' (60% confidence) (UNUSED)
- Line 252: unused function 'check_duplicate_kwargs' (60% confidence) (UNUSED)

#### error_wrappers.py
- Line 21: unused class 'ErrorDict' (60% confidence) (UNUSED)

#### fields.py
- Line 86: unused import 'ValidatorsList' (90% confidence) (UNUSED)
- Line 92: unused variable 'ValidateReturn' (60% confidence) (UNUSED)
- Line 93: unused variable 'LocStr' (60% confidence) (UNUSED)
- Line 94: unused variable 'BoolUndefined' (60% confidence) (UNUSED)

#### main.py
- Line 76: unused import 'ValidatorListDict' (90% confidence) (UNUSED)
- Line 284: unused attribute '__signature__' (60% confidence) (UNUSED)
- Line 815: unused method 'update_forward_refs' (60% confidence) (UNUSED)

#### mypy.py
- Line 3: unused import 'TypingType' (90% confidence) (UNUSED)

#### networks.py
- Line 56: unused class 'HostParts' (60% confidence) (UNUSED)

#### schema.py
- Line 147: unused variable 'm_nested_models' (60% confidence) (UNUSED)
- Line 801: unused variable 'json_scheme' (60% confidence) (UNUSED)

#### types.py
- Line 1119: unused method 'human_readable' (60% confidence) (UNUSED)

#### validators.py
- Line 55: unused variable 'AnyOrderedDict' (60% confidence) (UNUSED)

#### version.py
- Line 66: unused function 'check_pydantic_core_version' (60% confidence) (UNUSED)

#### __init__.py
- Line 113: unused class 'ErrorTypeInfo' (60% confidence) (UNUSED)
- Line 120: unused variable 'message_template_python' (60% confidence) (UNUSED)
- Line 122: unused variable 'example_message_python' (60% confidence) (UNUSED)
- Line 124: unused variable 'message_template_json' (60% confidence) (UNUSED)
- Line 126: unused variable 'example_message_json' (60% confidence) (UNUSED)
- Line 128: unused variable 'example_context' (60% confidence) (UNUSED)

#### core_schema.py
- Line 83: unused variable 'extra_fields_behavior' (60% confidence) (UNUSED)
- Line 84: unused variable 'typed_dict_total' (60% confidence) (UNUSED)
- Line 89: unused variable 'loc_by_alias' (60% confidence) (UNUSED)
- Line 96: unused variable 'str_max_length' (60% confidence) (UNUSED)
- Line 97: unused variable 'str_min_length' (60% confidence) (UNUSED)
- Line 98: unused variable 'str_strip_whitespace' (60% confidence) (UNUSED)
- Line 99: unused variable 'str_to_lower' (60% confidence) (UNUSED)
- Line 100: unused variable 'str_to_upper' (60% confidence) (UNUSED)
- Line 106: unused variable 'ser_json_inf_nan' (60% confidence) (UNUSED)
- Line 107: unused variable 'val_json_bytes' (60% confidence) (UNUSED)
- Line 109: unused variable 'hide_input_in_errors' (60% confidence) (UNUSED)
- Line 110: unused variable 'validation_error_cause' (60% confidence) (UNUSED)
- Line 113: unused variable 'cache_strings' (60% confidence) (UNUSED)
- Line 116: unused variable 'serialize_by_alias' (60% confidence) (UNUSED)
- Line 308: unused variable 'index_key' (100% confidence) (UNUSED)
- Line 378: unused function 'format_ser_schema' (60% confidence) (UNUSED)
- Line 417: unused function 'model_ser_schema' (60% confidence) (UNUSED)
- Line 447: unused function 'invalid_schema' (60% confidence) (UNUSED)
- Line 1469: unused function 'filter_seq_schema' (60% confidence) (UNUSED)
- Line 1534: unused function 'tuple_positional_schema' (60% confidence) (UNUSED)
- Line 1583: unused function 'tuple_variable_schema' (60% confidence) (UNUSED)
- Line 1875: unused function 'filter_dict_schema' (60% confidence) (UNUSED)
- Line 2170: unused variable 'outer_location' (100% confidence) (UNUSED)
- Line 4053: unsatisfiable 'if' condition (100% confidence) (UNUSED)
- Line 4231: unused function 'field_before_validator_function' (60% confidence) (UNUSED)
- Line 4240: unused function 'general_before_validator_function' (60% confidence) (UNUSED)
- Line 4249: unused function 'field_after_validator_function' (60% confidence) (UNUSED)
- Line 4258: unused function 'general_after_validator_function' (60% confidence) (UNUSED)
- Line 4267: unused function 'field_wrap_validator_function' (60% confidence) (UNUSED)
- Line 4278: unused function 'general_wrap_validator_function' (60% confidence) (UNUSED)
- Line 4287: unused function 'field_plain_validator_function' (60% confidence) (UNUSED)
- Line 4296: unused function 'general_plain_validator_function' (60% confidence) (UNUSED)
- Line 4313: unused variable 'FieldValidationInfo' (60% confidence) (UNUSED)

#### base_map_provider.py
- Line 8: unused variable 'GOOGLE_MAPS' (60% confidence) (UNUSED)

#### layer.py
- Line 141: unused method 'get_binary_data' (60% confidence) (UNUSED)

#### light_settings.py
- Line 4: unused class 'LightSettings' (60% confidence) (UNUSED)

#### color_scales.py
- Line 16: unused function 'assign_random_colors' (60% confidence) (UNUSED)

#### viewport_helpers.py
- Line 152: unused function 'compute_view' (60% confidence) (UNUSED)

#### __init__.py
- Line 1: unused function '_jupyter_nbextension_paths' (60% confidence) (UNUSED)

#### settings.py
- Line 37: unused method 'register_library' (60% confidence) (UNUSED)

#### widget.py
- Line 21: unused attribute 'handler_exception' (60% confidence) (UNUSED)
- Line 57: unused variable 'carto_key' (60% confidence) (UNUSED)
- Line 80: unused attribute 'handler_exception' (60% confidence) (UNUSED)
- Line 84: unused method 'on_hover' (60% confidence) (UNUSED)
- Line 87: unused method 'on_resize' (60% confidence) (UNUSED)
- Line 90: unused method 'on_view_state_change' (60% confidence) (UNUSED)
- Line 97: unused method 'on_drag_start' (60% confidence) (UNUSED)
- Line 100: unused method 'on_drag' (60% confidence) (UNUSED)
- Line 103: unused method 'on_drag_end' (60% confidence) (UNUSED)

#### checker.py
- Line 1362: unused variable 'ASYNCFOR' (60% confidence) (UNUSED)
- Line 1362: unused variable 'ASYNCWITH' (60% confidence) (UNUSED)
- Line 1362: unused variable 'DELETE' (60% confidence) (UNUSED)
- Line 1362: unused variable 'FOR' (60% confidence) (UNUSED)
- Line 1362: unused variable 'WHILE' (60% confidence) (UNUSED)
- Line 1362: unused variable 'WITH' (60% confidence) (UNUSED)
- Line 1362: unused variable 'WITHITEM' (60% confidence) (UNUSED)
- Line 1363: unused variable 'ASSIGN' (60% confidence) (UNUSED)
- Line 1363: unused variable 'EXPR' (60% confidence) (UNUSED)
- Line 1365: unused variable 'PASS' (60% confidence) (UNUSED)
- Line 1368: unused variable 'NAMECONSTANT' (60% confidence) (UNUSED)
- Line 1368: unused variable 'SET' (60% confidence) (UNUSED)
- Line 1368: unused variable 'STARRED' (60% confidence) (UNUSED)
- Line 1368: unused variable 'UNARYOP' (60% confidence) (UNUSED)
- Line 1369: unused variable 'NAMEDEXPR' (60% confidence) (UNUSED)
- Line 1371: unused method 'SUBSCRIPT' (60% confidence) (UNUSED)
- Line 1524: unused method 'CALL' (60% confidence) (UNUSED)
- Line 1713: unused method 'BINOP' (60% confidence) (UNUSED)
- Line 1735: unused variable 'EXTSLICE' (60% confidence) (UNUSED)
- Line 1735: unused variable 'SLICE' (60% confidence) (UNUSED)
- Line 1738: unused variable 'AUGLOAD' (60% confidence) (UNUSED)
- Line 1738: unused variable 'AUGSTORE' (60% confidence) (UNUSED)
- Line 1738: unused variable 'DEL' (60% confidence) (UNUSED)
- Line 1738: unused variable 'LOAD' (60% confidence) (UNUSED)
- Line 1738: unused variable 'PARAM' (60% confidence) (UNUSED)
- Line 1738: unused variable 'STORE' (60% confidence) (UNUSED)
- Line 1741: unused variable 'LSHIFT' (60% confidence) (UNUSED)
- Line 1741: unused variable 'MULT' (60% confidence) (UNUSED)
- Line 1741: unused variable 'RSHIFT' (60% confidence) (UNUSED)
- Line 1742: unused variable 'BITAND' (60% confidence) (UNUSED)
- Line 1742: unused variable 'BITOR' (60% confidence) (UNUSED)
- Line 1742: unused variable 'BITXOR' (60% confidence) (UNUSED)
- Line 1742: unused variable 'FLOORDIV' (60% confidence) (UNUSED)
- Line 1742: unused variable 'INVERT' (60% confidence) (UNUSED)
- Line 1742: unused variable 'NOT' (60% confidence) (UNUSED)
- Line 1742: unused variable 'UADD' (60% confidence) (UNUSED)
- Line 1742: unused variable 'USUB' (60% confidence) (UNUSED)
- Line 1743: unused variable 'GTE' (60% confidence) (UNUSED)
- Line 1743: unused variable 'IN' (60% confidence) (UNUSED)
- Line 1743: unused variable 'IS' (60% confidence) (UNUSED)
- Line 1743: unused variable 'ISNOT' (60% confidence) (UNUSED)
- Line 1743: unused variable 'LTE' (60% confidence) (UNUSED)
- Line 1743: unused variable 'NOTEQ' (60% confidence) (UNUSED)
- Line 1743: unused variable 'NOTIN' (60% confidence) (UNUSED)
- Line 1744: unused variable 'MATMULT' (60% confidence) (UNUSED)
- Line 1760: unused variable 'COMPREHENSION' (60% confidence) (UNUSED)
- Line 1760: unused variable 'FORMATTEDVALUE' (60% confidence) (UNUSED)
- Line 1764: unused method 'JOINEDSTR' (60% confidence) (UNUSED)
- Line 1820: unused variable 'IFEXP' (60% confidence) (UNUSED)
- Line 1822: unused method 'ASSERT' (60% confidence) (UNUSED)
- Line 1859: unused variable 'NONLOCAL' (60% confidence) (UNUSED)
- Line 1865: unused variable 'DICTCOMP' (60% confidence) (UNUSED)
- Line 1865: unused variable 'LISTCOMP' (60% confidence) (UNUSED)
- Line 1865: unused variable 'SETCOMP' (60% confidence) (UNUSED)
- Line 1904: unused variable 'BREAK' (60% confidence) (UNUSED)
- Line 1920: unused variable 'AWAIT' (60% confidence) (UNUSED)
- Line 1920: unused variable 'YIELDFROM' (60% confidence) (UNUSED)
- Line 1937: unused variable 'ASYNCFUNCTIONDEF' (60% confidence) (UNUSED)
- Line 1984: unused method 'ARGUMENTS' (60% confidence) (UNUSED)
- Line 1987: unused method 'ARG' (60% confidence) (UNUSED)
- Line 1990: unused method 'CLASSDEF' (60% confidence) (UNUSED)
- Line 2016: unused method 'AUGASSIGN' (60% confidence) (UNUSED)
- Line 2055: unused method 'IMPORTFROM' (60% confidence) (UNUSED)
- Line 2107: unused variable 'TRYSTAR' (60% confidence) (UNUSED)
- Line 2109: unused method 'EXCEPTHANDLER' (60% confidence) (UNUSED)
- Line 2154: unused method 'ANNASSIGN' (60% confidence) (UNUSED)
- Line 2165: unused method 'COMPARE' (60% confidence) (UNUSED)
- Line 2179: unused variable 'MATCH' (60% confidence) (UNUSED)
- Line 2179: unused variable 'MATCH_CASE' (60% confidence) (UNUSED)
- Line 2179: unused variable 'MATCHCLASS' (60% confidence) (UNUSED)
- Line 2179: unused variable 'MATCHOR' (60% confidence) (UNUSED)
- Line 2179: unused variable 'MATCHSEQUENCE' (60% confidence) (UNUSED)
- Line 2180: unused variable 'MATCHSINGLETON' (60% confidence) (UNUSED)
- Line 2180: unused variable 'MATCHVALUE' (60% confidence) (UNUSED)
- Line 2186: unused variable 'MATCHAS' (60% confidence) (UNUSED)
- Line 2186: unused variable 'MATCHMAPPING' (60% confidence) (UNUSED)
- Line 2186: unused variable 'MATCHSTAR' (60% confidence) (UNUSED)
- Line 2197: unused method 'TYPEVAR' (60% confidence) (UNUSED)
- Line 2201: unused variable 'PARAMSPEC' (60% confidence) (UNUSED)
- Line 2201: unused variable 'TYPEVARTUPLE' (60% confidence) (UNUSED)
- Line 2203: unused method 'TYPEALIAS' (60% confidence) (UNUSED)

#### console.py
- Line 40: unused function 'reset_color' (60% confidence) (UNUSED)

#### formatter.py
- Line 81: unused variable 'unicodeoutput' (60% confidence) (UNUSED)

#### img.py
- Line 386: unused variable 'unicodeoutput' (60% confidence) (UNUSED)
- Line 462: unused method '_get_char_width' (60% confidence) (UNUSED)

#### irc.py
- Line 94: unreachable code after 'return' (100% confidence) (UNUSED)

#### other.py
- Line 60: unused variable 'unicodeoutput' (60% confidence) (UNUSED)

#### lexer.py
- Line 886: unused variable 'it_index' (60% confidence) (UNUSED)
- Line 935: unused class 'ProfilingRegexLexer' (60% confidence) (UNUSED)

#### __init__.py
- Line 83: unused function 'find_lexer_class_by_name' (60% confidence) (UNUSED)

#### _stata_builtins.py
- Line 12: unused variable 'builtins_special' (60% confidence) (UNUSED)

#### agile.py
- Line 15: unused import 'Python3Lexer' (90% confidence) (UNUSED)
- Line 15: unused import 'Python3TracebackLexer' (90% confidence) (UNUSED)

#### asm.py
- Line 243: unused variable 'allocQual' (60% confidence) (UNUSED)

#### dsls.py
- Line 347: unused variable 'BroLexer' (60% confidence) (UNUSED)

#### html.py
- Line 608: unused variable 'JadeLexer' (60% confidence) (UNUSED)

#### jvm.py
- Line 177: unused variable 'alphaId' (60% confidence) (UNUSED)

#### lean.py
- Line 132: unused variable 'LeanLexer' (60% confidence) (UNUSED)

#### markup.py
- Line 1021: unused variable 'non_relative_protocols' (60% confidence) (UNUSED)

#### other.py
- Line 30: unused import 'BroLexer' (90% confidence) (UNUSED)

#### php.py
- Line 36: unused variable 'zephir_keywords' (60% confidence) (UNUSED)
- Line 37: unused variable 'zephir_type' (60% confidence) (UNUSED)

#### ptx.py
- Line 32: unused variable 'followsym' (60% confidence) (UNUSED)

#### python.py
- Line 413: unused variable 'Python3Lexer' (60% confidence) (UNUSED)
- Line 779: unused variable 'Python3TracebackLexer' (60% confidence) (UNUSED)

#### rdf.py
- Line 63: unused variable 'PN_CHARS_U' (60% confidence) (UNUSED)
- Line 366: unused variable 'PN_CHARS_U' (60% confidence) (UNUSED)

#### robotframework.py
- Line 450: unused method 'get_replaced_base' (60% confidence) (UNUSED)

#### sql.py
- Line 283: unused variable 're_error' (60% confidence) (UNUSED)

#### web.py
- Line 12: unused import 'JadeLexer' (90% confidence) (UNUSED)
- Line 22: unused variable 'JSONLexer' (60% confidence) (UNUSED)

#### webmisc.py
- Line 174: unused function 'pushstate_cdata_section_callback' (60% confidence) (UNUSED)
- Line 180: unused function 'pushstate_starttag_callback' (60% confidence) (UNUSED)
- Line 313: unused function 'pushstate_operator_attribute_callback' (60% confidence) (UNUSED)

#### regexopt.py
- Line 19: unused variable 'FIRST_ELEMENT' (60% confidence) (UNUSED)

#### sphinxext.py
- Line 65: unused variable 'has_content' (60% confidence) (UNUSED)
- Line 66: unused variable 'required_arguments' (60% confidence) (UNUSED)
- Line 67: unused variable 'optional_arguments' (60% confidence) (UNUSED)
- Line 68: unused variable 'final_argument_whitespace' (60% confidence) (UNUSED)
- Line 69: unused variable 'option_spec' (60% confidence) (UNUSED)

#### style.py
- Line 156: unused function 'list_styles' (60% confidence) (UNUSED)
- Line 203: unused variable 'web_style_gallery_exclude' (60% confidence) (UNUSED)

#### lilypond.py
- Line 29: unused variable 'web_style_gallery_exclude' (60% confidence) (UNUSED)

#### material.py
- Line 36: unused variable 'paleblue' (60% confidence) (UNUSED)
- Line 38: unused variable 'brown' (60% confidence) (UNUSED)

#### paraiso_dark.py
- Line 24: unused variable 'CURRENT_LINE' (60% confidence) (UNUSED)

#### paraiso_light.py
- Line 24: unused variable 'CURRENT_LINE' (60% confidence) (UNUSED)

#### token.py
- Line 85: unused function 'is_token_subtype' (60% confidence) (UNUSED)

#### unistring.py
- Line 14: unused variable 'Cc' (60% confidence) (UNUSED)
- Line 16: unused variable 'Cf' (60% confidence) (UNUSED)
- Line 18: unused variable 'Cn' (60% confidence) (UNUSED)
- Line 20: unused variable 'Co' (60% confidence) (UNUSED)
- Line 22: unused variable 'Cs' (60% confidence) (UNUSED)
- Line 26: unused variable 'Lm' (60% confidence) (UNUSED)
- Line 28: unused variable 'Lo' (60% confidence) (UNUSED)
- Line 34: unused variable 'Mc' (60% confidence) (UNUSED)
- Line 36: unused variable 'Me' (60% confidence) (UNUSED)
- Line 38: unused variable 'Mn' (60% confidence) (UNUSED)
- Line 40: unused variable 'Nd' (60% confidence) (UNUSED)
- Line 42: unused variable 'Nl' (60% confidence) (UNUSED)
- Line 44: unused variable 'No' (60% confidence) (UNUSED)
- Line 46: unused variable 'Pc' (60% confidence) (UNUSED)
- Line 48: unused variable 'Pd' (60% confidence) (UNUSED)
- Line 50: unused variable 'Pe' (60% confidence) (UNUSED)
- Line 52: unused variable 'Pf' (60% confidence) (UNUSED)
- Line 54: unused variable 'Pi' (60% confidence) (UNUSED)
- Line 56: unused variable 'Po' (60% confidence) (UNUSED)
- Line 58: unused variable 'Ps' (60% confidence) (UNUSED)
- Line 60: unused variable 'Sc' (60% confidence) (UNUSED)
- Line 62: unused variable 'Sk' (60% confidence) (UNUSED)
- Line 64: unused variable 'Sm' (60% confidence) (UNUSED)
- Line 66: unused variable 'So' (60% confidence) (UNUSED)
- Line 68: unused variable 'Zl' (60% confidence) (UNUSED)
- Line 70: unused variable 'Zp' (60% confidence) (UNUSED)
- Line 72: unused variable 'Zs' (60% confidence) (UNUSED)

#### __init__.py
- Line 39: unused function '_run_pylint_config' (60% confidence) (UNUSED)
- Line 116: unused attribute 'unraisablehook' (60% confidence) (UNUSED)

#### __pkginfo__.py
- Line 43: unused variable 'numversion' (60% confidence) (UNUSED)

#### async.py
- Line 46: unused method 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 54: unused method 'visit_asyncwith' (60% confidence) (UNUSED)

#### bad_chained_comparison.py
- Line 44: unused method 'visit_compare' (60% confidence) (UNUSED)

#### basic_checker.py
- Line 284: unused method 'visit_if' (60% confidence) (UNUSED)
- Line 290: unused method 'visit_ifexp' (60% confidence) (UNUSED)
- Line 425: unused method 'visit_expr' (60% confidence) (UNUSED)
- Line 526: unused method 'visit_lambda' (60% confidence) (UNUSED)
- Line 595: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 650: unused method 'visit_continue' (60% confidence) (UNUSED)
- Line 657: unused method 'visit_break' (60% confidence) (UNUSED)
- Line 671: unused method 'visit_raise' (60% confidence) (UNUSED)
- Line 723: unused method 'visit_assert' (60% confidence) (UNUSED)
- Line 736: unused method 'visit_dict' (60% confidence) (UNUSED)
- Line 751: unused method 'visit_set' (60% confidence) (UNUSED)
- Line 774: unused method 'leave_try' (60% confidence) (UNUSED)

#### basic_error_checker.py
- Line 238: unused method 'visit_starred' (60% confidence) (UNUSED)
- Line 297: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 362: unused method 'visit_yieldfrom' (60% confidence) (UNUSED)
- Line 366: unused method 'visit_continue' (60% confidence) (UNUSED)
- Line 370: unused method 'visit_break' (60% confidence) (UNUSED)
- Line 382: unused method 'visit_unaryop' (60% confidence) (UNUSED)
- Line 415: unused method 'visit_nonlocal' (60% confidence) (UNUSED)

#### comparison_checker.py
- Line 287: unused method 'visit_compare' (60% confidence) (UNUSED)

#### docstring_checker.py
- Line 150: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)

#### function_checker.py
- Line 33: unused method 'visit_asyncfunctiondef' (60% confidence) (UNUSED)

#### checker.py
- Line 334: unused method 'leave_module' (60% confidence) (UNUSED)
- Line 393: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)

#### pass_checker.py
- Line 23: unused method 'visit_pass' (60% confidence) (UNUSED)

#### class_checker.py
- Line 53: unused variable 'BUILTIN_DECORATORS' (60% confidence) (UNUSED)
- Line 1370: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 1695: unused variable 'leave_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 1731: unused method 'visit_assignattr' (60% confidence) (UNUSED)

#### special_methods_checker.py
- Line 195: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)

#### deprecated.py
- Line 145: unused method 'visit_importfrom' (60% confidence) (UNUSED)

#### design_analysis.py
- Line 598: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 634: unused variable 'leave_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 659: unused method 'visit_if' (60% confidence) (UNUSED)

#### ellipsis_checker.py
- Line 33: unused method 'visit_const' (60% confidence) (UNUSED)

#### exceptions.py
- Line 247: unused method 'visit_const' (60% confidence) (UNUSED)
- Line 260: unused variable 'visit_exceptioninstance' (60% confidence) (UNUSED)
- Line 270: unused method 'visit_tuple' (60% confidence) (UNUSED)
- Line 309: unused method 'visit_raise' (60% confidence) (UNUSED)
- Line 537: unused method 'visit_binop' (60% confidence) (UNUSED)
- Line 555: unused method 'visit_compare' (60% confidence) (UNUSED)
- Line 565: unused method 'visit_trystar' (60% confidence) (UNUSED)

#### imports.py
- Line 552: unused method 'visit_importfrom' (60% confidence) (UNUSED)
- Line 580: unused method 'leave_module' (60% confidence) (UNUSED)
- Line 649: unused variable 'visit_assignattr' (60% confidence) (UNUSED)
- Line 649: unused variable 'visit_ifexp' (60% confidence) (UNUSED)
- Line 650: unused variable 'visit_expr' (60% confidence) (UNUSED)
- Line 651: unused variable 'visit_if' (60% confidence) (UNUSED)

#### lambda_expressions.py
- Line 72: unused method 'visit_namedexpr' (60% confidence) (UNUSED)

#### logging.py
- Line 175: unused method 'visit_importfrom' (60% confidence) (UNUSED)

#### newstyle.py
- Line 117: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)

#### non_ascii_names.py
- Line 114: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 116: unused method 'visit_global' (60% confidence) (UNUSED)
- Line 162: unused method 'visit_importfrom' (60% confidence) (UNUSED)

#### implicit_booleaness_checker.py
- Line 163: unused method 'visit_unaryop' (60% confidence) (UNUSED)
- Line 177: unused method 'visit_compare' (60% confidence) (UNUSED)

#### not_checker.py
- Line 45: unused method 'visit_unaryop' (60% confidence) (UNUSED)

#### recommendation_checker.py
- Line 364: unused method 'visit_const' (60% confidence) (UNUSED)

#### refactoring_checker.py
- Line 699: unused method 'leave_module' (60% confidence) (UNUSED)
- Line 751: unused method 'visit_excepthandler' (60% confidence) (UNUSED)
- Line 884: unused method 'visit_if' (60% confidence) (UNUSED)
- Line 986: unused method 'visit_ifexp' (60% confidence) (UNUSED)
- Line 1045: unused method 'visit_raise' (60% confidence) (UNUSED)
- Line 1552: unused method 'visit_boolop' (60% confidence) (UNUSED)
- Line 1803: unused method 'visit_augassign' (60% confidence) (UNUSED)

#### spelling.py
- Line 48: unused method '_skip' (60% confidence) (UNUSED)
- Line 56: unused variable 'chunkers' (100% confidence) (UNUSED)
- Line 94: unused method '_skip' (60% confidence) (UNUSED)
- Line 104: unused method '_skip' (60% confidence) (UNUSED)
- Line 117: unused method '_skip' (60% confidence) (UNUSED)
- Line 454: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)

#### stdlib.py
- Line 697: unused method 'visit_unaryop' (60% confidence) (UNUSED)
- Line 702: unused method 'visit_if' (60% confidence) (UNUSED)
- Line 706: unused method 'visit_ifexp' (60% confidence) (UNUSED)
- Line 710: unused method 'visit_boolop' (60% confidence) (UNUSED)

#### strings.py
- Line 251: unused method 'visit_binop' (60% confidence) (UNUSED)
- Line 407: unused method 'visit_joinedstr' (60% confidence) (UNUSED)
- Line 722: unused attribute '_unicode_literals' (60% confidence) (UNUSED)
- Line 808: unused method 'visit_list' (60% confidence) (UNUSED)
- Line 812: unused method 'visit_set' (60% confidence) (UNUSED)
- Line 816: unused method 'visit_tuple' (60% confidence) (UNUSED)
- Line 999: unused method 'visit_const' (60% confidence) (UNUSED)

#### typecheck.py
- Line 1019: unused attribute 'wordchars' (60% confidence) (UNUSED)
- Line 1035: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 1070: unused method 'visit_assignattr' (60% confidence) (UNUSED)
- Line 1074: unused method 'visit_delattr' (60% confidence) (UNUSED)
- Line 1957: unused method 'visit_unaryop' (60% confidence) (UNUSED)
- Line 1964: unused method 'visit_binop' (60% confidence) (UNUSED)
- Line 2067: unused method '_visit_binop' (60% confidence) (UNUSED)
- Line 2075: unused method '_visit_augassign' (60% confidence) (UNUSED)
- Line 2103: unused method 'visit_compare' (60% confidence) (UNUSED)
- Line 2112: unused method 'visit_dict' (60% confidence) (UNUSED)
- Line 2123: unused method 'visit_set' (60% confidence) (UNUSED)
- Line 2134: unused method 'visit_subscript' (60% confidence) (UNUSED)
- Line 2225: unused method 'visit_await' (60% confidence) (UNUSED)
- Line 2312: unused method 'visit_asyncfor' (60% confidence) (UNUSED)
- Line 2316: unused method 'visit_yieldfrom' (60% confidence) (UNUSED)
- Line 2329: unused method 'visit_listcomp' (60% confidence) (UNUSED)
- Line 2334: unused method 'visit_dictcomp' (60% confidence) (UNUSED)
- Line 2339: unused method 'visit_setcomp' (60% confidence) (UNUSED)
- Line 2344: unused method 'visit_generatorexp' (60% confidence) (UNUSED)

#### unsupported_version.py
- Line 80: unused method 'visit_joinedstr' (60% confidence) (UNUSED)
- Line 88: unused method 'visit_namedexpr' (60% confidence) (UNUSED)
- Line 131: unused method 'visit_trystar' (60% confidence) (UNUSED)
- Line 140: unused method 'visit_excepthandler' (60% confidence) (UNUSED)
- Line 153: unused method 'visit_raise' (60% confidence) (UNUSED)
- Line 167: unused method 'visit_typealias' (60% confidence) (UNUSED)
- Line 176: unused method 'visit_typevar' (60% confidence) (UNUSED)
- Line 185: unused method 'visit_typevartuple' (60% confidence) (UNUSED)

#### utils.py
- Line 194: unused variable 'SUBSCRIPTABLE_CLASSES_PEP585' (60% confidence) (UNUSED)
- Line 289: unused function 'is_defined_in_scope' (60% confidence) (UNUSED)
- Line 1719: unused function 'is_classdef_type' (60% confidence) (UNUSED)

#### variables.py
- Line 52: unused variable 'TYPING_NAMES' (60% confidence) (UNUSED)
- Line 1389: unused method 'leave_for' (60% confidence) (UNUSED)
- Line 1405: unused method 'leave_module' (60% confidence) (UNUSED)
- Line 1459: unused method 'visit_lambda' (60% confidence) (UNUSED)
- Line 1463: unused method 'leave_lambda' (60% confidence) (UNUSED)
- Line 1468: unused method 'visit_generatorexp' (60% confidence) (UNUSED)
- Line 1472: unused method 'leave_generatorexp' (60% confidence) (UNUSED)
- Line 1477: unused method 'visit_dictcomp' (60% confidence) (UNUSED)
- Line 1481: unused method 'leave_dictcomp' (60% confidence) (UNUSED)
- Line 1486: unused method 'visit_setcomp' (60% confidence) (UNUSED)
- Line 1490: unused method 'leave_setcomp' (60% confidence) (UNUSED)
- Line 1590: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 1591: unused variable 'leave_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 1593: unused method 'visit_global' (60% confidence) (UNUSED)
- Line 1669: unused method 'visit_delname' (60% confidence) (UNUSED)
- Line 1687: unused method 'visit_excepthandler' (60% confidence) (UNUSED)
- Line 1703: unused method 'leave_excepthandler' (60% confidence) (UNUSED)
- Line 2092: unused method 'visit_importfrom' (60% confidence) (UNUSED)
- Line 2147: unused method 'visit_listcomp' (60% confidence) (UNUSED)
- Line 2151: unused method 'leave_listcomp' (60% confidence) (UNUSED)
- Line 2156: unused method 'leave_assign' (60% confidence) (UNUSED)
- Line 2159: unused method 'leave_with' (60% confidence) (UNUSED)
- Line 3388: unused method 'visit_subscript' (60% confidence) (UNUSED)
- Line 3425: unused method 'visit_const' (60% confidence) (UNUSED)

#### _breaking_changes.py
- Line 14: unused variable 'MESSAGE_MADE_DISABLED_BY_DEFAULT' (60% confidence) (UNUSED)
- Line 15: unused variable 'MESSAGE_MADE_ENABLED_BY_DEFAULT' (60% confidence) (UNUSED)
- Line 25: unused variable 'MESSAGE_IS_NOT_ENABLED' (60% confidence) (UNUSED)
- Line 26: unused variable 'MESSAGE_IS_DISABLED' (60% confidence) (UNUSED)
- Line 43: unused variable 'ENABLE_MESSAGE_IMPLICITLY' (60% confidence) (UNUSED)
- Line 46: unused variable 'DISABLE_MESSAGE_EXPLICITLY' (60% confidence) (UNUSED)
- Line 74: unused variable 'CONFIGURATION_BREAKING_CHANGES' (60% confidence) (UNUSED)

#### check_elif.py
- Line 48: unused method 'leave_module' (60% confidence) (UNUSED)
- Line 51: unused method 'visit_if' (60% confidence) (UNUSED)

#### code_style.py
- Line 119: unused method 'visit_dict' (60% confidence) (UNUSED)
- Line 133: unused method 'visit_if' (60% confidence) (UNUSED)

#### comparison_placement.py
- Line 55: unused method 'visit_compare' (60% confidence) (UNUSED)

#### confusing_elif.py
- Line 36: unused method 'visit_if' (60% confidence) (UNUSED)

#### consider_ternary_expression.py
- Line 30: unused method 'visit_if' (60% confidence) (UNUSED)

#### docparams.py
- Line 221: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 279: unused method 'visit_raise' (60% confidence) (UNUSED)
- Line 393: unused variable 'visit_yieldfrom' (60% confidence) (UNUSED)

#### docstyle.py
- Line 49: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)

#### magic_value.py
- Line 113: unused method 'visit_compare' (60% confidence) (UNUSED)

#### mccabe.py
- Line 92: unused variable 'visitAsyncFunctionDef' (60% confidence) (UNUSED)
- Line 97: unused variable 'visitAssert' (60% confidence) (UNUSED)
- Line 97: unused variable 'visitAssign' (60% confidence) (UNUSED)
- Line 97: unused variable 'visitAugAssign' (60% confidence) (UNUSED)
- Line 97: unused variable 'visitDelete' (60% confidence) (UNUSED)
- Line 97: unused variable 'visitRaise' (60% confidence) (UNUSED)
- Line 98: unused variable 'visitYield' (60% confidence) (UNUSED)
- Line 99: unused variable 'visitCall' (60% confidence) (UNUSED)
- Line 99: unused variable 'visitContinue' (60% confidence) (UNUSED)
- Line 99: unused variable 'visitImport' (60% confidence) (UNUSED)
- Line 99: unused variable 'visitPass' (60% confidence) (UNUSED)
- Line 99: unused variable 'visitSubscript' (60% confidence) (UNUSED)
- Line 100: unused variable 'visitBreak' (60% confidence) (UNUSED)
- Line 101: unused variable 'visitAwait' (60% confidence) (UNUSED)
- Line 101: unused variable 'visitExpr' (60% confidence) (UNUSED)
- Line 101: unused variable 'visitGlobal' (60% confidence) (UNUSED)
- Line 101: unused variable 'visitReturn' (60% confidence) (UNUSED)
- Line 107: unused variable 'visitAsyncWith' (60% confidence) (UNUSED)

#### no_self_use.py
- Line 57: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 99: unused variable 'leave_asyncfunctiondef' (60% confidence) (UNUSED)

#### private_import.py
- Line 57: unused method 'visit_importfrom' (60% confidence) (UNUSED)

#### redefined_loop_name.py
- Line 82: unused method 'leave_for' (60% confidence) (UNUSED)

#### redefined_variable_type.py
- Line 49: unused variable 'visit_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 50: unused variable 'leave_asyncfunctiondef' (60% confidence) (UNUSED)
- Line 50: unused variable 'leave_module' (60% confidence) (UNUSED)

#### set_membership.py
- Line 33: unused method 'visit_compare' (60% confidence) (UNUSED)

#### typing.py
- Line 236: unused method 'visit_annassign' (60% confidence) (UNUSED)
- Line 259: unused method 'visit_subscript' (60% confidence) (UNUSED)
- Line 417: unused method 'leave_module' (60% confidence) (UNUSED)

#### pylinter.py
- Line 324: unused attribute '_option_groups' (60% confidence) (UNUSED)

#### _deleted_message_ids.py
- Line 17: unused variable 'DELETED_MSGID_PREFIXES' (60% confidence) (UNUSED)

#### message_id_store.py
- Line 51: unused method 'get_msgid' (60% confidence) (UNUSED)

#### diadefslib.py
- Line 138: unused method 'visit_project' (60% confidence) (UNUSED)
- Line 152: unused method 'leave_project' (60% confidence) (UNUSED)
- Line 178: unused method 'visit_importfrom' (60% confidence) (UNUSED)

#### diagrams.py
- Line 112: unused method 'get_relationship' (60% confidence) (UNUSED)
- Line 199: unused method 'classe' (60% confidence) (UNUSED)

#### inspector.py
- Line 52: unused method 'init_counter' (60% confidence) (UNUSED)
- Line 127: unused method 'visit_project' (60% confidence) (UNUSED)
- Line 241: unused method 'visit_importfrom' (60% confidence) (UNUSED)

#### printer.py
- Line 33: unused variable 'RIGHT_TO_LEFT' (60% confidence) (UNUSED)

#### json_reporter.py
- Line 100: unused variable 'messageId' (60% confidence) (UNUSED)
- Line 105: unused variable 'absolutePath' (60% confidence) (UNUSED)
- Line 109: unused variable 'endColumn' (60% confidence) (UNUSED)

#### text_writer.py
- Line 25: unused variable 'BULLETS' (60% confidence) (UNUSED)
- Line 35: unused attribute 'list_level' (60% confidence) (UNUSED)
- Line 37: unused method 'visit_section' (60% confidence) (UNUSED)
- Line 45: unused method 'visit_evaluationsection' (60% confidence) (UNUSED)
- Line 52: unused method 'visit_title' (60% confidence) (UNUSED)
- Line 60: unused method 'visit_paragraph' (60% confidence) (UNUSED)
- Line 65: unused method 'visit_table' (60% confidence) (UNUSED)
- Line 99: unused method 'visit_verbatimtext' (60% confidence) (UNUSED)
- Line 106: unused method 'visit_text' (60% confidence) (UNUSED)

#### _run.py
- Line 26: unused class '_Run' (60% confidence) (UNUSED)

#### checker_test_case.py
- Line 34: unused method 'assertNoMessages' (60% confidence) (UNUSED)

#### configuration_test.py
- Line 49: unused function 'get_expected_configuration' (60% confidence) (UNUSED)
- Line 86: unused function 'get_expected_output' (60% confidence) (UNUSED)
- Line 135: unused function 'run_using_a_configuration_file' (60% confidence) (UNUSED)

#### lint_module_test.py
- Line 141: unused method 'runTest' (60% confidence) (UNUSED)

#### pyreverse.py
- Line 18: unused class 'PyreverseConfig' (60% confidence) (UNUSED)
- Line 74: unused variable 'output_formats' (60% confidence) (UNUSED)
- Line 75: unused variable 'command_line_args' (60% confidence) (UNUSED)
- Line 85: unused function 'get_functional_test_files' (60% confidence) (UNUSED)

#### unittest_linter.py
- Line 83: unused variable 'unused_args' (100% confidence) (UNUSED)
- Line 83: unused variable 'unused_kwargs' (100% confidence) (UNUSED)

#### utils.py
- Line 16: unused function '_patch_streams' (60% confidence) (UNUSED)
- Line 27: unused function '_test_sys_path' (60% confidence) (UNUSED)
- Line 40: unused function '_test_cwd' (60% confidence) (UNUSED)
- Line 53: unused function '_test_environ_pythonpath' (60% confidence) (UNUSED)

#### typing.py
- Line 54: unused variable 'isignored' (60% confidence) (UNUSED)
- Line 133: unused class 'GetProjectCallable' (60% confidence) (UNUSED)

#### linterstats.py
- Line 18: unused variable 'class_attribute' (60% confidence) (UNUSED)
- Line 19: unused variable 'class_const' (60% confidence) (UNUSED)
- Line 21: unused variable 'inlinevar' (60% confidence) (UNUSED)
- Line 27: unused variable 'typealias' (60% confidence) (UNUSED)
- Line 251: unused method 'get_code_count' (60% confidence) (UNUSED)

#### utils.py
- Line 58: unused variable 'GLOBAL_OPTION_NAMES' (60% confidence) (UNUSED)
- Line 66: unused variable 'T_GlobalOptionReturnTypes' (60% confidence) (UNUSED)

#### __init__.py
- Line 29: unused variable 'OLSEN_VERSION' (60% confidence) (UNUSED)
- Line 298: unused attribute '__safe_for_unpickling__' (60% confidence) (UNUSED)
- Line 310: unused attribute '__safe_for_unpickling__' (60% confidence) (UNUSED)
- Line 505: unused attribute '__safe_for_unpickling__' (60% confidence) (UNUSED)

#### reference.py
- Line 79: unused variable 'Local' (60% confidence) (UNUSED)

#### _core.py
- Line 21: unused variable 'EMPTY_PREVIOUS_RESOLVERS' (60% confidence) (UNUSED)

#### _internal_utils.py
- Line 19: unused variable 'HEADER_VALIDATORS' (60% confidence) (UNUSED)

#### adapters.py
- Line 74: unused variable 'DEFAULT_POOL_TIMEOUT' (60% confidence) (UNUSED)

#### auth.py
- Line 21: unused variable 'CONTENT_TYPE_FORM_URLENCODED' (60% confidence) (UNUSED)
- Line 22: unused variable 'CONTENT_TYPE_MULTI_PART' (60% confidence) (UNUSED)
- Line 99: unused class 'HTTPProxyAuth' (60% confidence) (UNUSED)
- Line 107: unused class 'HTTPDigestAuth' (60% confidence) (UNUSED)

#### compat.py
- Line 40: unused variable 'is_py2' (60% confidence) (UNUSED)
- Line 43: unused variable 'is_py3' (60% confidence) (UNUSED)

#### cookies.py
- Line 72: unused method 'has_header' (60% confidence) (UNUSED)
- Line 90: unused property 'unverifiable' (60% confidence) (UNUSED)
- Line 94: unused property 'origin_req_host' (60% confidence) (UNUSED)
- Line 277: unused method 'list_domains' (60% confidence) (UNUSED)
- Line 285: unused method 'list_paths' (60% confidence) (UNUSED)
- Line 293: unused method 'multiple_domains' (60% confidence) (UNUSED)
- Line 426: unused attribute '_cookies_lock' (60% confidence) (UNUSED)

#### exceptions.py
- Line 91: unused class 'URLRequired' (60% confidence) (UNUSED)

#### models.py
- Line 218: unused method 'deregister_hook' (60% confidence) (UNUSED)
- Line 776: unused property 'is_permanent_redirect' (60% confidence) (UNUSED)

#### structures.py
- Line 58: unused variable 'mappedvalue' (60% confidence) (UNUSED)

#### utils.py
- Line 126: unused function 'dict_to_sequence' (60% confidence) (UNUSED)
- Line 318: unused function 'from_key_val_list' (60% confidence) (UNUSED)
- Line 375: unused function 'parse_list_header' (60% confidence) (UNUSED)
- Line 467: unused function 'dict_from_cookiejar' (60% confidence) (UNUSED)
- Line 478: unused function 'add_dict_to_cookiejar' (60% confidence) (UNUSED)
- Line 489: unused function 'get_encodings_from_content' (60% confidence) (UNUSED)
- Line 591: unused function 'get_unicode_from_response' (60% confidence) (UNUSED)

#### _inspect.py
- Line 258: unused function 'is_object_one_of_types' (60% confidence) (UNUSED)

#### _null_file.py
- Line 12: unused variable '__n' (100% confidence) (UNUSED)
- Line 18: unused variable '__limit' (100% confidence) (UNUSED)
- Line 21: unused variable '__hint' (100% confidence) (UNUSED)
- Line 24: unused variable '__whence' (100% confidence) (UNUSED)
- Line 39: unused variable '__lines' (100% confidence) (UNUSED)
- Line 53: unused variable '__t' (100% confidence) (UNUSED)

#### align.py
- Line 234: unused class 'VerticalCenter' (60% confidence) (UNUSED)

#### box.py
- Line 296: unused variable 'SIMPLE_HEAD' (60% confidence) (UNUSED)
- Line 320: unused variable 'HORIZONTALS' (60% confidence) (UNUSED)
- Line 386: unused variable 'DOUBLE_EDGE' (60% confidence) (UNUSED)
- Line 397: unused variable 'MARKDOWN' (60% confidence) (UNUSED)

#### color.py
- Line 571: unused function 'parse_rgb_hex' (60% confidence) (UNUSED)

#### console.py
- Line 1803: unused method 'update_screen' (60% confidence) (UNUSED)
- Line 2200: unused method 'save_text' (60% confidence) (UNUSED)
- Line 2571: unused method 'save_svg' (60% confidence) (UNUSED)
- Line 2610: unused function '_svg_hash' (60% confidence) (UNUSED)

#### control.py
- Line 113: unused method 'move_to_column' (60% confidence) (UNUSED)

#### emoji.py
- Line 27: unused class 'Emoji' (60% confidence) (UNUSED)

#### errors.py
- Line 17: unused class 'StyleStackError' (60% confidence) (UNUSED)

#### highlighter.py
- Line 143: unused class 'ISO8601Highlighter' (60% confidence) (UNUSED)

#### layout.py
- Line 286: unused method 'add_split' (60% confidence) (UNUSED)
- Line 315: unused method 'unsplit' (60% confidence) (UNUSED)
- Line 328: unused method 'refresh_screen' (60% confidence) (UNUSED)

#### pretty.py
- Line 967: unused variable 'price' (60% confidence) (UNUSED)
- Line 969: unused variable 'reviews' (60% confidence) (UNUSED)

#### progress.py
- Line 517: unused attribute '_update_time' (60% confidence) (UNUSED)
- Line 551: unused class 'RenderableColumn' (60% confidence) (UNUSED)
- Line 594: unused method 'set_spinner' (60% confidence) (UNUSED)
- Line 831: unused class 'TotalFileSizeColumn' (60% confidence) (UNUSED)
- Line 840: unused class 'MofNCompleteColumn' (60% confidence) (UNUSED)
- Line 1156: unused property 'task_ids' (60% confidence) (UNUSED)
- Line 1401: unused method 'stop_task' (60% confidence) (UNUSED)
- Line 1642: unused method 'remove_task' (60% confidence) (UNUSED)
- Line 1708: unused variable 'task3' (60% confidence) (UNUSED)

#### progress_bar.py
- Line 55: unused attribute '_pulse_segments' (60% confidence) (UNUSED)
- Line 60: unused property 'percentage_completed' (60% confidence) (UNUSED)

#### prompt.py
- Line 328: unused class 'FloatPrompt' (60% confidence) (UNUSED)

#### scope.py
- Line 76: unused variable 'list_of_things' (60% confidence) (UNUSED)
- Line 77: unused variable 'dict_of_things' (60% confidence) (UNUSED)

#### segment.py
- Line 696: unused class 'SegmentLines' (60% confidence) (UNUSED)

#### style.py
- Line 280: unused property 'link_id' (60% confidence) (UNUSED)
- Line 648: unused method 'clear_meta_and_links' (60% confidence) (UNUSED)

#### terminal_theme.py
- Line 57: unused variable 'MONOKAI' (60% confidence) (UNUSED)
- Line 81: unused variable 'DIMMED_MONOKAI' (60% confidence) (UNUSED)
- Line 105: unused variable 'NIGHT_OWLISH' (60% confidence) (UNUSED)

#### traceback.py
- Line 192: unused attribute '_showtraceback' (60% confidence) (UNUSED)
- Line 195: unused attribute 'showsyntaxerror' (60% confidence) (UNUSED)

#### tree.py
- Line 11: unused variable 'GuideType' (60% confidence) (UNUSED)

#### _msvccompiler.py
- Line 218: unused variable 'shared_lib_format' (60% confidence) (UNUSED)
- Line 269: unused attribute 'preprocess_options' (60% confidence) (UNUSED)
- Line 497: unused variable 'dll_ext' (60% confidence) (UNUSED)

#### bcppcompiler.py
- Line 39: unused class 'BCPPCompiler' (60% confidence) (UNUSED)
- Line 63: unused variable 'shared_lib_format' (60% confidence) (UNUSED)
- Line 78: unused attribute 'preprocess_options' (60% confidence) (UNUSED)

#### ccompiler.py
- Line 77: unused variable 'shared_lib_format' (60% confidence) (UNUSED)
- Line 189: unused method '_check_macro_definitions' (60% confidence) (UNUSED)
- Line 244: unused method 'add_include_dir' (60% confidence) (UNUSED)
- Line 262: unused method 'add_library' (60% confidence) (UNUSED)
- Line 286: unused method 'add_library_dir' (60% confidence) (UNUSED)
- Line 301: unused method 'add_runtime_library_dir' (60% confidence) (UNUSED)
- Line 315: unused method 'add_link_object' (60% confidence) (UNUSED)
- Line 402: unused method '_prep_compile' (60% confidence) (UNUSED)
- Line 705: unused method 'link_shared_lib' (60% confidence) (UNUSED)
- Line 960: unused method 'shared_object_filename' (60% confidence) (UNUSED)

#### cmd.py
- Line 74: unused attribute '_dry_run' (60% confidence) (UNUSED)
- Line 154: unused method 'dump_options' (60% confidence) (UNUSED)

#### _framework_compat.py
- Line 45: unused variable 'homebrew_prefix' (60% confidence) (UNUSED)

#### bdist_rpm.py
- Line 175: unused attribute 'prep_script' (60% confidence) (UNUSED)
- Line 176: unused attribute 'build_script' (60% confidence) (UNUSED)
- Line 178: unused attribute 'clean_script' (60% confidence) (UNUSED)
- Line 179: unused attribute 'verify_script' (60% confidence) (UNUSED)
- Line 180: unused attribute 'pre_install' (60% confidence) (UNUSED)
- Line 181: unused attribute 'post_install' (60% confidence) (UNUSED)
- Line 182: unused attribute 'pre_uninstall' (60% confidence) (UNUSED)
- Line 183: unused attribute 'post_uninstall' (60% confidence) (UNUSED)
- Line 409: unused method '_dist_path' (60% confidence) (UNUSED)

#### build_ext.py
- Line 559: unused attribute '_built_objects' (60% confidence) (UNUSED)

#### check.py
- Line 130: unused attribute 'pep_references' (60% confidence) (UNUSED)
- Line 131: unused attribute 'rfc_references' (60% confidence) (UNUSED)

#### config.py
- Line 54: unused attribute 'noisy' (60% confidence) (UNUSED)
- Line 189: unused method 'search_cpp' (60% confidence) (UNUSED)
- Line 259: unused method 'try_run' (60% confidence) (UNUSED)
- Line 329: unused method 'check_lib' (60% confidence) (UNUSED)
- Line 354: unused method 'check_header' (60% confidence) (UNUSED)

#### install_egg_info.py
- Line 16: unused class 'install_egg_info' (60% confidence) (UNUSED)

#### sdist.py
- Line 134: unused attribute 'force_manifest' (60% confidence) (UNUSED)

#### core.py
- Line 52: unused variable 'setup_keywords' (60% confidence) (UNUSED)
- Line 77: unused variable 'extension_keywords' (60% confidence) (UNUSED)

#### cygwinccompiler.py
- Line 75: unused variable 'dylib_lib_extension' (60% confidence) (UNUSED)
- Line 77: unused variable 'shared_lib_format' (60% confidence) (UNUSED)
- Line 114: unused property 'gcc_version' (60% confidence) (UNUSED)
- Line 188: unused variable 'dll_extension' (60% confidence) (UNUSED)
- Line 261: unused class 'Mingw32CCompiler' (60% confidence) (UNUSED)

#### dep_util.py
- Line 33: unused function 'newer_pairwise' (60% confidence) (UNUSED)

#### dist.py
- Line 1001: unused method 'has_modules' (60% confidence) (UNUSED)
- Line 1193: unused method 'get_author' (60% confidence) (UNUSED)
- Line 1196: unused method 'get_author_email' (60% confidence) (UNUSED)
- Line 1199: unused method 'get_maintainer' (60% confidence) (UNUSED)
- Line 1202: unused method 'get_maintainer_email' (60% confidence) (UNUSED)
- Line 1228: unused method 'set_keywords' (60% confidence) (UNUSED)
- Line 1234: unused method 'set_platforms' (60% confidence) (UNUSED)
- Line 1240: unused method 'set_classifiers' (60% confidence) (UNUSED)
- Line 1250: unused method 'set_requires' (60% confidence) (UNUSED)
- Line 1260: unused method 'set_provides' (60% confidence) (UNUSED)
- Line 1271: unused method 'set_obsoletes' (60% confidence) (UNUSED)

#### extension.py
- Line 145: unused function 'read_setup_file' (60% confidence) (UNUSED)

#### fancy_getopt.py
- Line 25: unused variable 'neg_alias_re' (60% confidence) (UNUSED)
- Line 379: unused function 'fancy_getopt' (60% confidence) (UNUSED)

#### filelist.py
- Line 38: unused method 'set_allfiles' (60% confidence) (UNUSED)

#### msvc9compiler.py
- Line 347: unused variable 'shared_lib_format' (60% confidence) (UNUSED)
- Line 433: unused attribute 'preprocess_options' (60% confidence) (UNUSED)
- Line 666: unused variable 'dll_ext' (60% confidence) (UNUSED)

#### msvccompiler.py
- Line 252: unused variable 'shared_lib_format' (60% confidence) (UNUSED)
- Line 314: unused attribute 'preprocess_options' (60% confidence) (UNUSED)
- Line 555: unused variable 'dll_ext' (60% confidence) (UNUSED)
- Line 691: unused variable 'OldMSVCCompiler' (60% confidence) (UNUSED)

#### sysconfig.py
- Line 133: unused function '_get_python_inc_posix' (60% confidence) (UNUSED)
- Line 188: unused function '_get_python_inc_nt' (60% confidence) (UNUSED)

#### text_file.py
- Line 283: unused method 'unreadline' (60% confidence) (UNUSED)

#### unixccompiler.py
- Line 139: unused variable 'dylib_lib_extension' (60% confidence) (UNUSED)
- Line 140: unused variable 'xcode_stub_lib_extension' (60% confidence) (UNUSED)
- Line 141: unused variable 'shared_lib_format' (60% confidence) (UNUSED)
- Line 142: unused variable 'xcode_stub_lib_format' (60% confidence) (UNUSED)

#### util.py
- Line 69: unused function '_clear_cached_macosx_ver' (60% confidence) (UNUSED)
- Line 237: unused function 'grok_environment_error' (60% confidence) (UNUSED)

#### __init__.py
- Line 897: unused function 'invalidate_caches' (60% confidence) (UNUSED)

#### _meta.py
- Line 21: unused variable 'failobj' (100% confidence) (UNUSED)

#### abc.py
- Line 22: unused method 'resource_path' (60% confidence) (UNUSED)
- Line 130: unused method 'resource_path' (60% confidence) (UNUSED)

#### readers.py
- Line 19: unused method 'resource_path' (60% confidence) (UNUSED)
- Line 113: unused method 'resource_path' (60% confidence) (UNUSED)

#### simple.py
- Line 108: unused class 'TraversableReader' (60% confidence) (UNUSED)

#### context.py
- Line 20: unused function 'tarball_context' (60% confidence) (UNUSED)
- Line 72: unused function 'repo_context' (60% confidence) (UNUSED)

#### functools.py
- Line 40: unused function 'method_caller' (60% confidence) (UNUSED)
- Line 241: unused function 'result_invoke' (60% confidence) (UNUSED)
- Line 269: unused function 'call_aside' (60% confidence) (UNUSED)
- Line 341: unused variable 'attempt' (60% confidence) (UNUSED)
- Line 376: unused function 'print_yielded' (60% confidence) (UNUSED)
- Line 410: unused function 'assign_params' (60% confidence) (UNUSED)
- Line 442: unused function 'save_method_args' (60% confidence) (UNUSED)
- Line 488: unused function 'except_' (60% confidence) (UNUSED)

#### __init__.py
- Line 22: unused function 'multi_substitution' (60% confidence) (UNUSED)
- Line 317: unused method 'headless_camel_case' (60% confidence) (UNUSED)
- Line 323: unused method 'underscore_separated' (60% confidence) (UNUSED)
- Line 326: unused method 'dash_separated' (60% confidence) (UNUSED)
- Line 329: unused method 'space_separated' (60% confidence) (UNUSED)
- Line 376: unused method 'from_class_name' (60% confidence) (UNUSED)
- Line 385: unused function 'simple_html_strip' (60% confidence) (UNUSED)
- Line 407: unused class 'SeparatedValues' (60% confidence) (UNUSED)
- Line 428: unused class 'Stripper' (60% confidence) (UNUSED)
- Line 510: unused function 'normalize_newlines' (60% confidence) (UNUSED)

#### more.py
- Line 3102: unused attribute 'timed_out' (60% confidence) (UNUSED)
- Line 3110: unused attribute 'timed_out' (60% confidence) (UNUSED)
- Line 3815: unused attribute 'items_seen' (60% confidence) (UNUSED)
- Line 3822: unused attribute 'items_seen' (60% confidence) (UNUSED)

#### ordered_set.py
- Line 472: unused method 'symmetric_difference_update' (60% confidence) (UNUSED)

#### _manylinux.py
- Line 28: unused variable 'EM_S390' (60% confidence) (UNUSED)
- Line 30: unused variable 'EM_X86_64' (60% confidence) (UNUSED)
- Line 53: unused attribute 'e_ident_version' (60% confidence) (UNUSED)
- Line 54: unused attribute 'e_ident_osabi' (60% confidence) (UNUSED)
- Line 55: unused attribute 'e_ident_abiversion' (60% confidence) (UNUSED)
- Line 56: unused attribute 'e_ident_pad' (60% confidence) (UNUSED)
- Line 61: unused attribute 'e_type' (60% confidence) (UNUSED)
- Line 63: unused attribute 'e_version' (60% confidence) (UNUSED)
- Line 64: unused attribute 'e_entry' (60% confidence) (UNUSED)
- Line 66: unused attribute 'e_shoff' (60% confidence) (UNUSED)
- Line 68: unused attribute 'e_ehsize' (60% confidence) (UNUSED)
- Line 71: unused attribute 'e_shentsize' (60% confidence) (UNUSED)
- Line 72: unused attribute 'e_shnum' (60% confidence) (UNUSED)
- Line 73: unused attribute 'e_shstrndx' (60% confidence) (UNUSED)

#### specifiers.py
- Line 269: unused method '_compare_not_equal' (60% confidence) (UNUSED)
- Line 272: unused method '_compare_less_than_equal' (60% confidence) (UNUSED)
- Line 275: unused method '_compare_greater_than_equal' (60% confidence) (UNUSED)
- Line 280: unused method '_compare_less_than' (60% confidence) (UNUSED)
- Line 283: unused method '_compare_greater_than' (60% confidence) (UNUSED)
- Line 407: unused method '_compare_compatible' (60% confidence) (UNUSED)
- Line 469: unused method '_compare_not_equal' (60% confidence) (UNUSED)
- Line 473: unused method '_compare_less_than_equal' (60% confidence) (UNUSED)
- Line 481: unused method '_compare_greater_than_equal' (60% confidence) (UNUSED)
- Line 491: unused method '_compare_less_than' (60% confidence) (UNUSED)
- Line 517: unused method '_compare_greater_than' (60% confidence) (UNUSED)
- Line 549: unused method '_compare_arbitrary' (60% confidence) (UNUSED)

#### version.py
- Line 33: unused variable 'VersionComparisonMethod' (60% confidence) (UNUSED)
- Line 163: unused property 'is_devrelease' (60% confidence) (UNUSED)
- Line 376: unused property 'is_devrelease' (60% confidence) (UNUSED)

#### __init__.py
- Line 162: unused variable 'core_builtin_exprs' (60% confidence) (UNUSED)

#### common.py
- Line 167: unused variable 'hex_integer' (60% confidence) (UNUSED)
- Line 212: unused variable 'fnumber' (60% confidence) (UNUSED)
- Line 240: unused variable 'ipv6_address' (60% confidence) (UNUSED)
- Line 247: unused variable 'mac_address' (60% confidence) (UNUSED)
- Line 306: unused variable 'iso8601_date' (60% confidence) (UNUSED)
- Line 311: unused variable 'iso8601_datetime' (60% confidence) (UNUSED)
- Line 413: unused variable 'convertToInteger' (60% confidence) (UNUSED)
- Line 414: unused variable 'convertToFloat' (60% confidence) (UNUSED)
- Line 415: unused variable 'convertToDate' (60% confidence) (UNUSED)
- Line 416: unused variable 'convertToDatetime' (60% confidence) (UNUSED)
- Line 417: unused variable 'stripHTMLTags' (60% confidence) (UNUSED)
- Line 418: unused variable 'upcaseTokens' (60% confidence) (UNUSED)
- Line 419: unused variable 'downcaseTokens' (60% confidence) (UNUSED)

#### core.py
- Line 167: unused function 'enable_diag' (60% confidence) (UNUSED)
- Line 174: unused function 'disable_diag' (60% confidence) (UNUSED)
- Line 197: unused variable 'w_line' (60% confidence) (UNUSED)
- Line 779: unused variable 'MATCH' (60% confidence) (UNUSED)
- Line 913: unused variable 'MATCH' (60% confidence) (UNUSED)
- Line 2145: unused method 'create_diagram' (60% confidence) (UNUSED)
- Line 2191: unused variable 'setDefaultWhitespaceChars' (60% confidence) (UNUSED)
- Line 2193: unused variable 'setResultsName' (60% confidence) (UNUSED)
- Line 2194: unused variable 'setBreak' (60% confidence) (UNUSED)
- Line 2196: unused variable 'addParseAction' (60% confidence) (UNUSED)
- Line 2197: unused variable 'addCondition' (60% confidence) (UNUSED)
- Line 2198: unused variable 'setFailAction' (60% confidence) (UNUSED)
- Line 2202: unused variable 'enableLeftRecursion' (60% confidence) (UNUSED)
- Line 2203: unused variable 'enablePackrat' (60% confidence) (UNUSED)
- Line 2205: unused variable 'scanString' (60% confidence) (UNUSED)
- Line 2206: unused variable 'searchString' (60% confidence) (UNUSED)
- Line 2207: unused variable 'transformString' (60% confidence) (UNUSED)
- Line 2208: unused variable 'setWhitespaceChars' (60% confidence) (UNUSED)
- Line 2209: unused variable 'parseWithTabs' (60% confidence) (UNUSED)
- Line 2210: unused variable 'setDebugActions' (60% confidence) (UNUSED)
- Line 2211: unused variable 'setDebug' (60% confidence) (UNUSED)
- Line 2214: unused variable 'parseFile' (60% confidence) (UNUSED)
- Line 2215: unused variable 'runTests' (60% confidence) (UNUSED)
- Line 2216: unused variable 'ignoreWhitespace' (60% confidence) (UNUSED)
- Line 2469: unused variable 'setDefaultKeywordChars' (60% confidence) (UNUSED)
- Line 2715: unused attribute 'bodyCharsOrig' (60% confidence) (UNUSED)
- Line 2718: unused attribute 'bodyCharsOrig' (60% confidence) (UNUSED)
- Line 3753: unused variable 'ignoreWhitespace' (60% confidence) (UNUSED)
- Line 4433: unused variable 'ignoreWhitespace' (60% confidence) (UNUSED)
- Line 5359: unused variable 'ignoreWhitespace' (60% confidence) (UNUSED)

#### __init__.py
- Line 313: unused attribute 'extracted_diagram_names' (60% confidence) (UNUSED)
- Line 327: unused method 'generate_unnamed' (60% confidence) (UNUSED)

#### exceptions.py
- Line 217: unused variable 'markInputline' (60% confidence) (UNUSED)

#### helpers.py
- Line 644: unused attribute 'tag_body' (60% confidence) (UNUSED)

#### results.py
- Line 162: unused attribute '_modal' (60% confidence) (UNUSED)
- Line 755: unused variable 'asDict' (60% confidence) (UNUSED)

#### testing.py
- Line 20: unused class 'reset_pyparsing_context' (60% confidence) (UNUSED)
- Line 141: unused method 'assertParseAndCheckList' (60% confidence) (UNUSED)
- Line 155: unused method 'assertParseAndCheckDict' (60% confidence) (UNUSED)
- Line 169: unused method 'assertRunTestResults' (60% confidence) (UNUSED)
- Line 232: unused method 'assertRaisesParseException' (60% confidence) (UNUSED)

#### unicode.py
- Line 290: unused class 'CJK' (60% confidence) (UNUSED)
- Line 338: unused attribute 'BMP' (60% confidence) (UNUSED)
- Line 341: unused attribute 'العربية' (60% confidence) (UNUSED)
- Line 342: unused attribute '中文' (60% confidence) (UNUSED)
- Line 343: unused attribute 'кириллица' (60% confidence) (UNUSED)
- Line 344: unused attribute 'Ελληνικά' (60% confidence) (UNUSED)
- Line 345: unused attribute 'עִברִית' (60% confidence) (UNUSED)
- Line 346: unused attribute '日本語' (60% confidence) (UNUSED)
- Line 347: unused attribute '漢字' (60% confidence) (UNUSED)
- Line 348: unused attribute 'カタカナ' (60% confidence) (UNUSED)
- Line 349: unused attribute 'ひらがな' (60% confidence) (UNUSED)
- Line 350: unused attribute '한국어' (60% confidence) (UNUSED)
- Line 351: unused attribute 'ไทย' (60% confidence) (UNUSED)
- Line 352: unused attribute 'देवनागरी' (60% confidence) (UNUSED)

#### typing_extensions.py
- Line 771: unused attribute '__tree_hash__' (60% confidence) (UNUSED)
- Line 1085: unused attribute '__optional_keys__' (60% confidence) (UNUSED)
- Line 1360: unused attribute '__orig_class__' (60% confidence) (UNUSED)

#### archive_util.py
- Line 160: unused attribute 'chown' (60% confidence) (UNUSED)

#### build_meta.py
- Line 108: unused function '_get_immediate_subdirectories' (60% confidence) (UNUSED)
- Line 225: unused method '__dist_info_args' (60% confidence) (UNUSED)

#### build.py
- Line 36: unused class 'SubCommand' (60% confidence) (UNUSED)

#### easy_install.py
- Line 186: unused attribute '_dry_run' (60% confidence) (UNUSED)
- Line 1120: unused variable 'eggloc' (60% confidence) (UNUSED)
- Line 1509: unused variable 'bmlen' (60% confidence) (UNUSED)
- Line 1915: unused function 'is_sh' (60% confidence) (UNUSED)
- Line 1925: unused function 'nt_quote_arg' (60% confidence) (UNUSED)

#### editable_wheel.py
- Line 105: unused class 'editable_wheel' (60% confidence) (UNUSED)
- Line 371: unused class 'EditableStrategy' (60% confidence) (UNUSED)

#### egg_info.py
- Line 550: unused attribute 'force_manifest' (60% confidence) (UNUSED)
- Line 684: unused function 'warn_depends_obsolete' (60% confidence) (UNUSED)
- Line 712: unused function 'write_setup_requirements' (60% confidence) (UNUSED)
- Line 718: unused function 'write_toplevel_names' (60% confidence) (UNUSED)
- Line 728: unused function 'overwrite_arg' (60% confidence) (UNUSED)
- Line 740: unused function 'write_entries' (60% confidence) (UNUSED)
- Line 746: unused function 'get_pkg_info_revision' (60% confidence) (UNUSED)

#### install_egg_info.py
- Line 11: unused class 'install_egg_info' (60% confidence) (UNUSED)

#### saveopts.py
- Line 4: unused class 'saveopts' (60% confidence) (UNUSED)

#### test.py
- Line 26: unused class 'ScanningLoader' (60% confidence) (UNUSED)
- Line 128: unused method 'with_project_on_sys_path' (60% confidence) (UNUSED)
- Line 136: unused variable 'include_dists' (100% confidence) (UNUSED)

#### upload_docs.py
- Line 32: unused class 'upload_docs' (60% confidence) (UNUSED)

#### fastjsonschema_exceptions.py
- Line 48: unused class 'JsonSchemaDefinitionException' (60% confidence) (UNUSED)

#### fastjsonschema_validations.py
- Line 44: unused variable 'data__buildsystem_len' (60% confidence) (UNUSED)
- Line 55: unused variable 'data__buildsystem__requires_len' (60% confidence) (UNUSED)
- Line 74: unused variable 'data__buildsystem__backendpath_len' (60% confidence) (UNUSED)
- Line 117: unused variable 'data__platforms_len' (60% confidence) (UNUSED)
- Line 128: unused variable 'data__provides_len' (60% confidence) (UNUSED)
- Line 142: unused variable 'data__obsoletes_len' (60% confidence) (UNUSED)
- Line 161: unused variable 'data__scriptfiles_len' (60% confidence) (UNUSED)
- Line 172: unused variable 'data__eagerresources_len' (60% confidence) (UNUSED)
- Line 186: unused variable 'data__packages_len' (60% confidence) (UNUSED)
- Line 259: unused variable 'data__packagedata_val_len' (60% confidence) (UNUSED)
- Line 311: unused variable 'data__excludepackagedata_val_len' (60% confidence) (UNUSED)
- Line 349: unused variable 'data__namespacepackages_len' (60% confidence) (UNUSED)
- Line 363: unused variable 'data__pymodules_len' (60% confidence) (UNUSED)
- Line 386: unused variable 'data__datafiles_val_len' (60% confidence) (UNUSED)
- Line 414: unused variable 'data__licensefiles_len' (60% confidence) (UNUSED)
- Line 511: unused variable 'data__dynamic__readme_len' (60% confidence) (UNUSED)
- Line 545: unused variable 'data__file_len' (60% confidence) (UNUSED)
- Line 596: unused variable 'data__find__where_len' (60% confidence) (UNUSED)
- Line 607: unused variable 'data__find__exclude_len' (60% confidence) (UNUSED)
- Line 618: unused variable 'data__find__include_len' (60% confidence) (UNUSED)
- Line 701: unused variable 'data__readme_len' (60% confidence) (UNUSED)
- Line 716: unused variable 'data__readme_len' (60% confidence) (UNUSED)
- Line 731: unused variable 'data__readme_len' (60% confidence) (UNUSED)
- Line 760: unused variable 'data__license_len' (60% confidence) (UNUSED)
- Line 775: unused variable 'data__license_len' (60% confidence) (UNUSED)
- Line 795: unused variable 'data__authors_len' (60% confidence) (UNUSED)
- Line 796: unused variable 'data__authors_x' (60% confidence) (UNUSED)
- Line 805: unused variable 'data__maintainers_len' (60% confidence) (UNUSED)
- Line 806: unused variable 'data__maintainers_x' (60% confidence) (UNUSED)
- Line 815: unused variable 'data__keywords_len' (60% confidence) (UNUSED)
- Line 826: unused variable 'data__classifiers_len' (60% confidence) (UNUSED)
- Line 892: unused variable 'data__dependencies_len' (60% confidence) (UNUSED)
- Line 893: unused variable 'data__dependencies_x' (60% confidence) (UNUSED)
- Line 911: unused variable 'data__optionaldependencies_val_len' (60% confidence) (UNUSED)
- Line 912: unused variable 'data__optionaldependencies_val_x' (60% confidence) (UNUSED)
- Line 935: unused variable 'data__dynamic_len' (60% confidence) (UNUSED)

#### formats.py
- Line 47: unused function 'pep440' (60% confidence) (UNUSED)
- Line 87: unused function 'pep508_versionspec' (60% confidence) (UNUSED)
- Line 103: unused function 'pep517_backend_reference' (60% confidence) (UNUSED)
- Line 226: unused function 'python_module_name' (60% confidence) (UNUSED)
- Line 230: unused function 'python_entrypoint_group' (60% confidence) (UNUSED)
- Line 234: unused function 'python_entrypoint_name' (60% confidence) (UNUSED)
- Line 244: unused function 'python_entrypoint_reference' (60% confidence) (UNUSED)

#### setupcfg.py
- Line 525: unused variable 'strict_mode' (60% confidence) (UNUSED)
- Line 718: unused method 'parse_section_entry_points' (60% confidence) (UNUSED)
- Line 730: unused method 'parse_section_package_data' (60% confidence) (UNUSED)
- Line 737: unused method 'parse_section_exclude_package_data' (60% confidence) (UNUSED)
- Line 744: unused method 'parse_section_extras_require' (60% confidence) (UNUSED)
- Line 756: unused method 'parse_section_data_files' (60% confidence) (UNUSED)

#### depends.py
- Line 73: unused method 'is_present' (60% confidence) (UNUSED)

#### dist.py
- Line 57: unused function '_get_unpatched' (60% confidence) (UNUSED)
- Line 264: unused function 'check_nsp' (60% confidence) (UNUSED)
- Line 289: unused function 'check_extras' (60% confidence) (UNUSED)
- Line 308: unused function 'assert_bool' (60% confidence) (UNUSED)
- Line 315: unused function 'invalid_unless_false' (60% confidence) (UNUSED)
- Line 336: unused function 'check_specifier' (60% confidence) (UNUSED)
- Line 347: unused function 'check_entry_points' (60% confidence) (UNUSED)
- Line 355: unused function 'check_test_suite' (60% confidence) (UNUSED)
- Line 360: unused function 'check_package_data' (60% confidence) (UNUSED)
- Line 375: unused function 'check_packages' (60% confidence) (UNUSED)
- Line 499: unused method '_validate_metadata' (60% confidence) (UNUSED)
- Line 916: unused method '_finalize_setup_keywords' (60% confidence) (UNUSED)
- Line 1084: unused method '_exclude_packages' (60% confidence) (UNUSED)
- Line 1118: unused method 'get_cmdline_options' (60% confidence) (UNUSED)
- Line 1169: unused variable 'buildinfo' (60% confidence) (UNUSED)

#### errors.py
- Line 11: unused variable 'ByteCompileError' (60% confidence) (UNUSED)
- Line 15: unused variable 'ExecError' (60% confidence) (UNUSED)
- Line 20: unused variable 'ModuleError' (60% confidence) (UNUSED)
- Line 22: unused variable 'PlatformError' (60% confidence) (UNUSED)
- Line 24: unused variable 'SetupError' (60% confidence) (UNUSED)

#### extension.py
- Line 25: unused variable 'have_pyrex' (60% confidence) (UNUSED)

#### __init__.py
- Line 51: unused method 'create_module' (60% confidence) (UNUSED)

#### msvc.py
- Line 194: unused function 'msvc14_get_vc_env' (60% confidence) (UNUSED)
- Line 1093: unused class 'EnvironmentInfo' (60% confidence) (UNUSED)
- Line 1622: unused method 'return_env' (60% confidence) (UNUSED)

#### package_index.py
- Line 286: unused variable 'ca_bundle' (100% confidence) (UNUSED)
- Line 286: unused variable 'verify_ssl' (100% confidence) (UNUSED)
- Line 748: unused variable 'blksize' (100% confidence) (UNUSED)
- Line 864: unused variable 'pop_prefix' (100% confidence) (UNUSED)
- Line 1094: unused function 'fix_sf_url' (60% confidence) (UNUSED)

#### six.py
- Line 43: unused variable 'class_types' (60% confidence) (UNUSED)
- Line 47: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 51: unused variable 'class_types' (60% confidence) (UNUSED)
- Line 57: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 68: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 71: unused variable 'MAXSIZE' (60% confidence) (UNUSED)
- Line 236: unused method 'create_module' (60% confidence) (UNUSED)
- Line 506: unused variable 'robotparser' (60% confidence) (UNUSED)
- Line 515: unused function 'add_move' (60% confidence) (UNUSED)
- Line 520: unused function 'remove_move' (60% confidence) (UNUSED)
- Line 568: unused variable 'create_bound_method' (60% confidence) (UNUSED)
- Line 570: unused function 'create_unbound_method' (60% confidence) (UNUSED)
- Line 578: unused function 'create_bound_method' (60% confidence) (UNUSED)
- Line 581: unused function 'create_unbound_method' (60% confidence) (UNUSED)
- Line 594: unused variable 'get_method_function' (60% confidence) (UNUSED)
- Line 595: unused variable 'get_method_self' (60% confidence) (UNUSED)
- Line 596: unused variable 'get_function_closure' (60% confidence) (UNUSED)
- Line 597: unused variable 'get_function_code' (60% confidence) (UNUSED)
- Line 598: unused variable 'get_function_defaults' (60% confidence) (UNUSED)
- Line 599: unused variable 'get_function_globals' (60% confidence) (UNUSED)
- Line 615: unused variable 'viewkeys' (60% confidence) (UNUSED)
- Line 617: unused variable 'viewvalues' (60% confidence) (UNUSED)
- Line 619: unused variable 'viewitems' (60% confidence) (UNUSED)
- Line 633: unused variable 'viewkeys' (60% confidence) (UNUSED)
- Line 635: unused variable 'viewvalues' (60% confidence) (UNUSED)
- Line 637: unused variable 'viewitems' (60% confidence) (UNUSED)
- Line 655: unused variable 'int2byte' (60% confidence) (UNUSED)
- Line 657: unused variable 'byte2int' (60% confidence) (UNUSED)
- Line 658: unused variable 'indexbytes' (60% confidence) (UNUSED)
- Line 659: unused variable 'iterbytes' (60% confidence) (UNUSED)
- Line 681: unused variable 'int2byte' (60% confidence) (UNUSED)
- Line 683: unused function 'byte2int' (60% confidence) (UNUSED)
- Line 686: unused function 'indexbytes' (60% confidence) (UNUSED)
- Line 688: unused variable 'iterbytes' (60% confidence) (UNUSED)
- Line 699: unused method 'assertCountEqual' (60% confidence) (UNUSED)
- Line 711: unused method 'assertNotRegex' (60% confidence) (UNUSED)
- Line 758: unused variable 'from_value' (100% confidence) (UNUSED)
- Line 861: unused function 'with_metaclass' (60% confidence) (UNUSED)
- Line 868: unused variable 'this_bases' (100% confidence) (UNUSED)
- Line 880: unused variable 'this_bases' (100% confidence) (UNUSED)
- Line 963: unused function 'python_2_unicode_compatible' (60% confidence) (UNUSED)

#### lib.py
- Line 63: unused method 'setUpAll' (60% confidence) (UNUSED)

#### test_util.py
- Line 82: unused variable 'rfull2' (60% confidence) (UNUSED)

#### driver.py
- Line 66: unused variable 'drivermanager' (100% confidence) (UNUSED)

#### sphinxext.py
- Line 68: unused variable 'option_spec' (60% confidence) (UNUSED)
- Line 76: unused variable 'has_content' (60% confidence) (UNUSED)

#### test_extension.py
- Line 34: unused method 'get_args_and_data' (60% confidence) (UNUSED)
- Line 38: unused class 'BrokenExtension' (60% confidence) (UNUSED)

#### __init__.py
- Line 285: unused variable 'experimental_dialog' (60% confidence) (UNUSED)
- Line 287: unused variable 'experimental_user' (60% confidence) (UNUSED)
- Line 291: unused variable 'experimental_get_query_params' (60% confidence) (UNUSED)
- Line 298: unused variable 'experimental_set_query_params' (60% confidence) (UNUSED)

#### auth_util.py
- Line 43: unused variable 'expires_in' (100% confidence) (UNUSED)

#### echo.py
- Line 105: unused function '_get_initial_indent' (60% confidence) (UNUSED)

#### page_config.py
- Line 238: unused attribute 'favicon' (60% confidence) (UNUSED)
- Line 285: unused attribute 'get_help_url' (60% confidence) (UNUSED)
- Line 287: unused attribute 'hide_get_help' (60% confidence) (UNUSED)
- Line 291: unused attribute 'report_a_bug_url' (60% confidence) (UNUSED)
- Line 293: unused attribute 'hide_report_a_bug' (60% confidence) (UNUSED)
- Line 297: unused attribute 'about_section_md' (60% confidence) (UNUSED)

#### local_component_registry.py
- Line 76: unused method 'get_module_name' (60% confidence) (UNUSED)
- Line 80: unused method 'get_component' (60% confidence) (UNUSED)
- Line 83: unused method 'get_components' (60% confidence) (UNUSED)

#### base_component_registry.py
- Line 56: unused method 'get_module_name' (60% confidence) (UNUSED)
- Line 73: unused method 'get_component' (60% confidence) (UNUSED)
- Line 90: unused method 'get_components' (60% confidence) (UNUSED)

#### component_registry.py
- Line 125: unused class 'ComponentRegistry' (60% confidence) (UNUSED)

#### config.py
- Line 340: unused function '_delete_option' (60% confidence) (UNUSED)
- Line 386: unused function '_global_development_mode' (60% confidence) (UNUSED)
- Line 460: unused function '_logger_log_level' (60% confidence) (UNUSED)
- Line 473: unused function '_logger_message_format' (60% confidence) (UNUSED)
- Line 491: unused function '_logger_enable_rich' (60% confidence) (UNUSED)
- Line 695: unused function '_server_cookie_secret' (60% confidence) (UNUSED)
- Line 707: unused function '_server_headless' (60% confidence) (UNUSED)
- Line 745: unused function '_server_address' (60% confidence) (UNUSED)
- Line 915: unused function '_browser_server_port' (60% confidence) (UNUSED)
- Line 1601: unused attribute 'is_development_mode' (60% confidence) (UNUSED)

#### snowflake_connection.py
- Line 243: unused attribute 'paramstyle' (60% confidence) (UNUSED)
- Line 488: unused property 'raw_connection' (60% confidence) (UNUSED)

#### snowpark_connection.py
- Line 189: unused method 'safe_session' (60% confidence) (UNUSED)

#### dataframe_util.py
- Line 354: unused function 'is_pandas_data_object' (60% confidence) (UNUSED)

#### delta_generator.py
- Line 108: unused variable 'MAX_DELTA_BYTES' (60% confidence) (UNUSED)

#### delta_generator_singletons.py
- Line 93: unused property 'sidebar_dg' (60% confidence) (UNUSED)

#### development.py
- Line 21: unused variable 'is_development_mode' (60% confidence) (UNUSED)

#### alert.py
- Line 95: unused attribute 'pixel_width' (60% confidence) (UNUSED)
- Line 97: unused attribute 'use_stretch' (60% confidence) (UNUSED)
- Line 165: unused attribute 'pixel_width' (60% confidence) (UNUSED)
- Line 167: unused attribute 'use_stretch' (60% confidence) (UNUSED)
- Line 236: unused attribute 'pixel_width' (60% confidence) (UNUSED)
- Line 238: unused attribute 'use_stretch' (60% confidence) (UNUSED)
- Line 306: unused attribute 'pixel_width' (60% confidence) (UNUSED)
- Line 308: unused attribute 'use_stretch' (60% confidence) (UNUSED)

#### arrow.py
- Line 581: unused attribute 'editing_mode' (60% confidence) (UNUSED)
- Line 928: unused attribute 'has_name' (60% confidence) (UNUSED)

#### code.py
- Line 105: unused attribute 'show_line_numbers' (60% confidence) (UNUSED)

#### empty.py
- Line 102: unused method '_skeleton' (60% confidence) (UNUSED)

#### exception.py
- Line 137: unused attribute 'is_warning' (60% confidence) (UNUSED)
- Line 142: unused attribute 'pixel_width' (60% confidence) (UNUSED)
- Line 144: unused attribute 'use_stretch' (60% confidence) (UNUSED)

#### heading.py
- Line 285: unused attribute 'hide_anchor' (60% confidence) (UNUSED)

#### iframe.py
- Line 236: unused attribute 'has_width' (60% confidence) (UNUSED)

#### json.py
- Line 127: unused attribute 'max_expand_depth' (60% confidence) (UNUSED)

#### layouts.py
- Line 373: unused attribute 'show_border' (60% confidence) (UNUSED)

#### color_util.py
- Line 52: unused variable 'CSSColorStr' (60% confidence) (UNUSED)

#### js_number.py
- Line 39: unused variable 'MIN_VALUE' (60% confidence) (UNUSED)

#### pandas_styler_utils.py
- Line 240: unused attribute 'display_values' (60% confidence) (UNUSED)

#### markdown.py
- Line 139: unused attribute 'allow_html' (60% confidence) (UNUSED)
- Line 202: unused attribute 'allow_html' (60% confidence) (UNUSED)
- Line 203: unused attribute 'is_caption' (60% confidence) (UNUSED)

#### metric.py
- Line 194: unused attribute 'show_border' (60% confidence) (UNUSED)

#### plotly_chart.py
- Line 54: unused import 'BaseFigure' (90% confidence) (UNUSED)
- Line 163: unused variable 'point_indices' (60% confidence) (UNUSED)
- Line 165: unused variable 'lasso' (60% confidence) (UNUSED)

#### vega_charts.py
- Line 299: unused attribute 'has_name' (60% confidence) (UNUSED)

#### button.py
- Line 852: unused attribute 'ignore_rerun' (60% confidence) (UNUSED)
- Line 854: unused attribute 'ignore_rerun' (60% confidence) (UNUSED)
- Line 944: unused attribute 'external' (60% confidence) (UNUSED)

#### chat.py
- Line 99: unused variable 'HUMAN' (60% confidence) (UNUSED)
- Line 609: unused attribute 'max_upload_size_mb' (60% confidence) (UNUSED)

#### data_editor.py
- Line 936: unused attribute 'editing_mode' (60% confidence) (UNUSED)

#### file_uploader.py
- Line 445: unused attribute 'max_upload_size_mb' (60% confidence) (UNUSED)
- Line 448: unused attribute 'multiple_files' (60% confidence) (UNUSED)

#### errors.py
- Line 34: unused class 'CustomComponentError' (60% confidence) (UNUSED)
- Line 40: unused class 'DeprecationError' (60% confidence) (UNUSED)
- Line 60: unused class 'NoStaticFiles' (60% confidence) (UNUSED)
- Line 152: unused class 'StreamlitModuleNotFoundError' (60% confidence) (UNUSED)

#### streamlit_callback_handler.py
- Line 103: unused variable 'is_complete' (100% confidence) (UNUSED)
- Line 171: unused property 'last_tool' (60% confidence) (UNUSED)
- Line 316: unused attribute '_history_parent' (60% confidence) (UNUSED)
- Line 319: unused attribute '_max_thought_containers' (60% confidence) (UNUSED)
- Line 332: unused method '_get_last_completed_thought' (60% confidence) (UNUSED)
- Line 398: unused method 'on_agent_finish' (60% confidence) (UNUSED)

#### file_util.py
- Line 33: unused function 'get_encoded_file_data' (60% confidence) (UNUSED)

#### git_util.py
- Line 129: unused method 'is_github_repo' (60% confidence) (UNUSED)

#### logger.py
- Line 79: unused attribute 'default_msec_format' (60% confidence) (UNUSED)

#### platform.py
- Line 23: unused function 'post_parent_message' (60% confidence) (UNUSED)

#### Alert_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_WidthConfig__pb2' (90% confidence) (UNUSED)

#### ArrowNamedDataSet_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_Arrow__pb2' (90% confidence) (UNUSED)

#### ArrowVegaLiteChart_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_Arrow__pb2' (90% confidence) (UNUSED)
- Line 16: unused import 'streamlit_dot_proto_dot_ArrowNamedDataSet__pb2' (90% confidence) (UNUSED)

#### AudioInput_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### BackMsg_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_ClientState__pb2' (90% confidence) (UNUSED)
- Line 16: unused import 'streamlit_dot_proto_dot_Common__pb2' (90% confidence) (UNUSED)

#### ButtonGroup_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### CameraInput_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### Checkbox_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### ClientState_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_WidgetStates__pb2' (90% confidence) (UNUSED)

#### ColorPicker_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### DataFrame_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_Common__pb2' (90% confidence) (UNUSED)

#### DateInput_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### Delta_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_Block__pb2' (90% confidence) (UNUSED)
- Line 16: unused import 'streamlit_dot_proto_dot_Element__pb2' (90% confidence) (UNUSED)
- Line 17: unused import 'streamlit_dot_proto_dot_NamedDataSet__pb2' (90% confidence) (UNUSED)
- Line 18: unused import 'streamlit_dot_proto_dot_ArrowNamedDataSet__pb2' (90% confidence) (UNUSED)

#### Element_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_Alert__pb2' (90% confidence) (UNUSED)
- Line 16: unused import 'streamlit_dot_proto_dot_Arrow__pb2' (90% confidence) (UNUSED)
- Line 17: unused import 'streamlit_dot_proto_dot_Audio__pb2' (90% confidence) (UNUSED)
- Line 18: unused import 'streamlit_dot_proto_dot_AudioInput__pb2' (90% confidence) (UNUSED)
- Line 19: unused import 'streamlit_dot_proto_dot_Balloons__pb2' (90% confidence) (UNUSED)
- Line 20: unused import 'streamlit_dot_proto_dot_ArrowVegaLiteChart__pb2' (90% confidence) (UNUSED)
- Line 21: unused import 'streamlit_dot_proto_dot_BokehChart__pb2' (90% confidence) (UNUSED)
- Line 22: unused import 'streamlit_dot_proto_dot_Button__pb2' (90% confidence) (UNUSED)
- Line 23: unused import 'streamlit_dot_proto_dot_ButtonGroup__pb2' (90% confidence) (UNUSED)
- Line 24: unused import 'streamlit_dot_proto_dot_DownloadButton__pb2' (90% confidence) (UNUSED)
- Line 25: unused import 'streamlit_dot_proto_dot_CameraInput__pb2' (90% confidence) (UNUSED)
- Line 26: unused import 'streamlit_dot_proto_dot_ChatInput__pb2' (90% confidence) (UNUSED)
- Line 27: unused import 'streamlit_dot_proto_dot_Checkbox__pb2' (90% confidence) (UNUSED)
- Line 28: unused import 'streamlit_dot_proto_dot_Code__pb2' (90% confidence) (UNUSED)
- Line 29: unused import 'streamlit_dot_proto_dot_ColorPicker__pb2' (90% confidence) (UNUSED)
- Line 30: unused import 'streamlit_dot_proto_dot_DataFrame__pb2' (90% confidence) (UNUSED)
- Line 31: unused import 'streamlit_dot_proto_dot_DateInput__pb2' (90% confidence) (UNUSED)
- Line 32: unused import 'streamlit_dot_proto_dot_DeckGlJsonChart__pb2' (90% confidence) (UNUSED)
- Line 33: unused import 'streamlit_dot_proto_dot_DocString__pb2' (90% confidence) (UNUSED)
- Line 34: unused import 'streamlit_dot_proto_dot_Empty__pb2' (90% confidence) (UNUSED)
- Line 35: unused import 'streamlit_dot_proto_dot_Exception__pb2' (90% confidence) (UNUSED)
- Line 36: unused import 'streamlit_dot_proto_dot_Favicon__pb2' (90% confidence) (UNUSED)
- Line 37: unused import 'streamlit_dot_proto_dot_FileUploader__pb2' (90% confidence) (UNUSED)
- Line 38: unused import 'streamlit_dot_proto_dot_GraphVizChart__pb2' (90% confidence) (UNUSED)
- Line 39: unused import 'streamlit_dot_proto_dot_Html__pb2' (90% confidence) (UNUSED)
- Line 40: unused import 'streamlit_dot_proto_dot_IFrame__pb2' (90% confidence) (UNUSED)
- Line 41: unused import 'streamlit_dot_proto_dot_Image__pb2' (90% confidence) (UNUSED)
- Line 42: unused import 'streamlit_dot_proto_dot_Json__pb2' (90% confidence) (UNUSED)
- Line 43: unused import 'streamlit_dot_proto_dot_LinkButton__pb2' (90% confidence) (UNUSED)
- Line 44: unused import 'streamlit_dot_proto_dot_NumberInput__pb2' (90% confidence) (UNUSED)
- Line 45: unused import 'streamlit_dot_proto_dot_Markdown__pb2' (90% confidence) (UNUSED)
- Line 46: unused import 'streamlit_dot_proto_dot_Metric__pb2' (90% confidence) (UNUSED)
- Line 47: unused import 'streamlit_dot_proto_dot_MultiSelect__pb2' (90% confidence) (UNUSED)
- Line 48: unused import 'streamlit_dot_proto_dot_PageLink__pb2' (90% confidence) (UNUSED)
- Line 49: unused import 'streamlit_dot_proto_dot_PlotlyChart__pb2' (90% confidence) (UNUSED)
- Line 50: unused import 'streamlit_dot_proto_dot_Components__pb2' (90% confidence) (UNUSED)
- Line 51: unused import 'streamlit_dot_proto_dot_Progress__pb2' (90% confidence) (UNUSED)
- Line 52: unused import 'streamlit_dot_proto_dot_Snow__pb2' (90% confidence) (UNUSED)
- Line 53: unused import 'streamlit_dot_proto_dot_Spinner__pb2' (90% confidence) (UNUSED)
- Line 54: unused import 'streamlit_dot_proto_dot_Radio__pb2' (90% confidence) (UNUSED)
- Line 55: unused import 'streamlit_dot_proto_dot_Selectbox__pb2' (90% confidence) (UNUSED)
- Line 56: unused import 'streamlit_dot_proto_dot_Skeleton__pb2' (90% confidence) (UNUSED)
- Line 57: unused import 'streamlit_dot_proto_dot_Slider__pb2' (90% confidence) (UNUSED)
- Line 58: unused import 'streamlit_dot_proto_dot_Text__pb2' (90% confidence) (UNUSED)
- Line 59: unused import 'streamlit_dot_proto_dot_TextArea__pb2' (90% confidence) (UNUSED)
- Line 60: unused import 'streamlit_dot_proto_dot_TextInput__pb2' (90% confidence) (UNUSED)
- Line 61: unused import 'streamlit_dot_proto_dot_TimeInput__pb2' (90% confidence) (UNUSED)
- Line 62: unused import 'streamlit_dot_proto_dot_Toast__pb2' (90% confidence) (UNUSED)
- Line 63: unused import 'streamlit_dot_proto_dot_VegaLiteChart__pb2' (90% confidence) (UNUSED)
- Line 64: unused import 'streamlit_dot_proto_dot_Video__pb2' (90% confidence) (UNUSED)
- Line 65: unused import 'streamlit_dot_proto_dot_Heading__pb2' (90% confidence) (UNUSED)

#### Exception_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_WidthConfig__pb2' (90% confidence) (UNUSED)

#### FileUploader_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### ForwardMsg_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_AutoRerun__pb2' (90% confidence) (UNUSED)
- Line 16: unused import 'streamlit_dot_proto_dot_Common__pb2' (90% confidence) (UNUSED)
- Line 17: unused import 'streamlit_dot_proto_dot_Delta__pb2' (90% confidence) (UNUSED)
- Line 18: unused import 'streamlit_dot_proto_dot_GitInfo__pb2' (90% confidence) (UNUSED)
- Line 19: unused import 'streamlit_dot_proto_dot_Logo__pb2' (90% confidence) (UNUSED)
- Line 20: unused import 'streamlit_dot_proto_dot_Navigation__pb2' (90% confidence) (UNUSED)
- Line 21: unused import 'streamlit_dot_proto_dot_NewSession__pb2' (90% confidence) (UNUSED)
- Line 22: unused import 'streamlit_dot_proto_dot_PageConfig__pb2' (90% confidence) (UNUSED)
- Line 23: unused import 'streamlit_dot_proto_dot_PageInfo__pb2' (90% confidence) (UNUSED)
- Line 24: unused import 'streamlit_dot_proto_dot_PageProfile__pb2' (90% confidence) (UNUSED)
- Line 25: unused import 'streamlit_dot_proto_dot_PageNotFound__pb2' (90% confidence) (UNUSED)
- Line 26: unused import 'streamlit_dot_proto_dot_PagesChanged__pb2' (90% confidence) (UNUSED)
- Line 27: unused import 'streamlit_dot_proto_dot_ParentMessage__pb2' (90% confidence) (UNUSED)
- Line 28: unused import 'streamlit_dot_proto_dot_SessionEvent__pb2' (90% confidence) (UNUSED)
- Line 29: unused import 'streamlit_dot_proto_dot_SessionStatus__pb2' (90% confidence) (UNUSED)
- Line 30: unused import 'streamlit_dot_proto_dot_AuthRedirect__pb2' (90% confidence) (UNUSED)

#### Metric_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### MetricsEvent_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_PageProfile__pb2' (90% confidence) (UNUSED)

#### MultiSelect_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### NamedDataSet_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_DataFrame__pb2' (90% confidence) (UNUSED)

#### Navigation_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_AppPage__pb2' (90% confidence) (UNUSED)

#### NewSession_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_AppPage__pb2' (90% confidence) (UNUSED)
- Line 16: unused import 'streamlit_dot_proto_dot_SessionStatus__pb2' (90% confidence) (UNUSED)

#### NumberInput_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### openmetrics_data_model_pb2.py
- Line 15: unused import 'google_dot_protobuf_dot_timestamp__pb2' (90% confidence) (UNUSED)

#### PagesChanged_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_AppPage__pb2' (90% confidence) (UNUSED)

#### Radio_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### Selectbox_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### SessionEvent_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_Exception__pb2' (90% confidence) (UNUSED)

#### Slider_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### TextArea_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### TextInput_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### TimeInput_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_LabelVisibilityMessage__pb2' (90% confidence) (UNUSED)

#### VegaLiteChart_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_DataFrame__pb2' (90% confidence) (UNUSED)
- Line 16: unused import 'streamlit_dot_proto_dot_NamedDataSet__pb2' (90% confidence) (UNUSED)

#### WidgetStates_pb2.py
- Line 15: unused import 'streamlit_dot_proto_dot_Common__pb2' (90% confidence) (UNUSED)
- Line 16: unused import 'streamlit_dot_proto_dot_Components__pb2' (90% confidence) (UNUSED)

#### app_session.py
- Line 696: unused attribute 'run_on_save' (60% confidence) (UNUSED)
- Line 697: unused attribute 'script_is_running' (60% confidence) (UNUSED)
- Line 705: unused attribute 'script_changed_on_disk' (60% confidence) (UNUSED)
- Line 717: unused attribute 'script_run_id' (60% confidence) (UNUSED)
- Line 744: unused attribute 'streamlit_version' (60% confidence) (UNUSED)
- Line 746: unused attribute 'server_os' (60% confidence) (UNUSED)
- Line 747: unused attribute 'has_display' (60% confidence) (UNUSED)
- Line 751: unused attribute 'run_on_save' (60% confidence) (UNUSED)
- Line 752: unused attribute 'script_is_running' (60% confidence) (UNUSED)
- Line 919: unused attribute 'max_cached_message_age' (60% confidence) (UNUSED)
- Line 920: unused attribute 'allow_run_on_save' (60% confidence) (UNUSED)
- Line 921: unused attribute 'hide_top_bar' (60% confidence) (UNUSED)
- Line 923: unused attribute 'hide_sidebar_nav' (60% confidence) (UNUSED)
- Line 924: unused attribute 'toolbar_mode' (60% confidence) (UNUSED)

#### cached_message_replay.py
- Line 129: unused attribute '_cache_type' (60% confidence) (UNUSED)

#### legacy_cache_api.py
- Line 39: unused variable 'suppress_st_warning' (100% confidence) (UNUSED)

#### forward_msg_cache.py
- Line 98: unused attribute 'ref_hash' (60% confidence) (UNUSED)

#### forward_msg_queue.py
- Line 35: unused method 'on_before_enqueue_msg' (60% confidence) (UNUSED)

#### fragment.py
- Line 283: unused attribute '__signature__' (60% confidence) (UNUSED)

#### metrics_util.py
- Line 468: unused attribute '__signature__' (60% confidence) (UNUSED)
- Line 486: unused attribute 'headless' (60% confidence) (UNUSED)

#### runtime.py
- Line 81: unused variable 'command_line' (60% confidence) (UNUSED)
- Line 190: unused attribute '_loop_coroutine_task' (60% confidence) (UNUSED)
- Line 299: unused attribute '_loop_coroutine_task' (60% confidence) (UNUSED)
- Line 396: unused method 'create_session' (60% confidence) (UNUSED)

#### runtime_util.py
- Line 54: unused class 'BadDurationStringError' (60% confidence) (UNUSED)

#### magic_funcs.py
- Line 22: unused function 'transparent_write' (60% confidence) (UNUSED)

#### secrets.py
- Line 71: unused method 'set_missing_attr_message' (60% confidence) (UNUSED)
- Line 75: unused method 'set_missing_key_message' (60% confidence) (UNUSED)
- Line 79: unused method 'set_no_secrets_found_message' (60% confidence) (UNUSED)
- Line 83: unused method 'set_error_parsing_file_at_path_message' (60% confidence) (UNUSED)
- Line 89: unused method 'set_subfolder_path_is_not_a_folder_message' (60% confidence) (UNUSED)
- Line 95: unused method 'set_invalid_secret_path_message' (60% confidence) (UNUSED)
- Line 224: unused method 'set_suppress_print_error_on_exception' (60% confidence) (UNUSED)
- Line 225: unused variable 'suppress_print_error_on_exception' (100% confidence) (UNUSED)

#### session_manager.py
- Line 83: unused class 'SessionStorageError' (60% confidence) (UNUSED)
- Line 318: unused method 'num_sessions' (60% confidence) (UNUSED)

#### query_params_proxy.py
- Line 84: unused variable 'keys_and_values' (100% confidence) (UNUSED)
- Line 169: unused variable 'keys_and_values' (100% confidence) (UNUSED)

#### session_state.py
- Line 308: unused method 'set_key_id_mapping' (60% confidence) (UNUSED)
- Line 315: unused method 'get_key_from_id' (60% confidence) (UNUSED)

#### app_test.py
- Line 220: unused method 'from_function' (60% confidence) (UNUSED)

#### element_tree.py
- Line 321: unused attribute 'trigger_value' (60% confidence) (UNUSED)
- Line 421: unused method 'uncheck' (60% confidence) (UNUSED)
- Line 433: unused variable 'show_line_numbers' (60% confidence) (UNUSED)
- Line 564: unused variable 'is_markdown' (60% confidence) (UNUSED)
- Line 566: unused variable 'is_warning' (60% confidence) (UNUSED)
- Line 574: unused attribute 'is_markdown' (60% confidence) (UNUSED)
- Line 588: unused variable 'hide_anchor' (60% confidence) (UNUSED)
- Line 641: unused variable 'is_caption' (60% confidence) (UNUSED)
- Line 642: unused variable 'allow_html' (60% confidence) (UNUSED)
- Line 764: unused method 'unselect' (60% confidence) (UNUSED)
- Line 857: unused method 'unselect' (60% confidence) (UNUSED)
- Line 907: unused attribute 'double_value' (60% confidence) (UNUSED)
- Line 1052: unused method 'select_index' (60% confidence) (UNUSED)
- Line 1127: unused method 'set_range' (60% confidence) (UNUSED)
- Line 1180: unused method 'set_range' (60% confidence) (UNUSED)

#### asizeof.py
- Line 2091: unused method 'exclude_types' (60% confidence) (UNUSED)
- Line 2520: unused function 'amapped' (60% confidence) (UNUSED)
- Line 2729: unused function 'basicsize' (60% confidence) (UNUSED)
- Line 2800: unused function 'named_refs' (60% confidence) (UNUSED)

#### event_based_path_watcher.py
- Line 71: unused method 'close_all' (60% confidence) (UNUSED)
- Line 399: unused method 'on_created' (60% confidence) (UNUSED)
- Line 402: unused method 'on_modified' (60% confidence) (UNUSED)
- Line 405: unused method 'on_moved' (60% confidence) (UNUSED)

#### polling_path_watcher.py
- Line 38: unused method 'close_all' (60% confidence) (UNUSED)

#### bootstrap.py
- Line 42: unused variable 'signal_number' (100% confidence) (UNUSED)
- Line 42: unused variable 'stack_frame' (100% confidence) (UNUSED)

#### cli.py
- Line 162: unused function 'main_version' (60% confidence) (UNUSED)
- Line 177: unused function 'main_docs' (60% confidence) (UNUSED)
- Line 186: unused function 'main_hello' (60% confidence) (UNUSED)
- Line 197: unused function 'main_run' (60% confidence) (UNUSED)
- Line 311: unused function 'config_show' (60% confidence) (UNUSED)
- Line 332: unused function 'activate_reset' (60% confidence) (UNUSED)
- Line 350: unused function 'test_prog_name' (60% confidence) (UNUSED)
- Line 368: unused function 'main_init' (60% confidence) (UNUSED)

#### oidc_mixin.py
- Line 31: unused variable 'client_cls' (60% confidence) (UNUSED)
- Line 101: unused variable 'oauth2_client_cls' (60% confidence) (UNUSED)
- Line 102: unused variable 'framework_integration_cls' (60% confidence) (UNUSED)

#### server.py
- Line 102: unused variable 'MESSAGE_ENDPOINT' (60% confidence) (UNUSED)
- Line 457: unused property 'browser_is_connected' (60% confidence) (UNUSED)

#### websocket_headers.py
- Line 29: unused function '_get_websocket_headers' (60% confidence) (UNUSED)

#### __init__.py
- Line 114: unused variable 'delay_since_first_attempt' (60% confidence) (UNUSED)
- Line 121: unused attribute 'delay_since_first_attempt' (60% confidence) (UNUSED)

#### stop.py
- Line 41: unused variable 'StopBaseT' (60% confidence) (UNUSED)

#### wait.py
- Line 44: unused variable 'WaitBaseT' (60% confidence) (UNUSED)

#### encoder.py
- Line 296: unused method '_dump_pathlib_path' (60% confidence) (UNUSED)

#### ordered.py
- Line 6: unused class 'TomlOrderedDecoder' (60% confidence) (UNUSED)
- Line 12: unused class 'TomlOrderedEncoder' (60% confidence) (UNUSED)

#### _types.py
- Line 33: unused class 'WrapperType' (60% confidence) (UNUSED)

#### container.py
- Line 364: unused method '_insert_after' (60% confidence) (UNUSED)

#### exceptions.py
- Line 35: unused class 'MixedArrayTypesError' (60% confidence) (UNUSED)
- Line 90: unused class 'InvalidNumberOrDateError' (60% confidence) (UNUSED)

#### items.py
- Line 460: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 503: unused method 'is_inline_table' (60% confidence) (UNUSED)
- Line 541: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 564: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 602: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 695: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 761: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 858: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 970: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 1046: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 1172: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 1554: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 1694: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 1791: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 1860: unused property 'discriminant' (60% confidence) (UNUSED)
- Line 1948: unused property 'discriminant' (60% confidence) (UNUSED)

#### toml_char.py
- Line 30: unused method 'is_int_float_char' (60% confidence) (UNUSED)

#### toml_file.py
- Line 18: unused class 'TOMLFile' (60% confidence) (UNUSED)

#### autoreload.py
- Line 152: unused function 'add_reload_hook' (60% confidence) (UNUSED)

#### concurrent.py
- Line 42: unused class 'ReturnValueIgnoredError' (60% confidence) (UNUSED)
- Line 69: unused variable 'cancel_futures' (100% confidence) (UNUSED)

#### curl_httpclient.py
- Line 156: unused variable 'num_handles' (60% confidence) (UNUSED)
- Line 168: unused variable 'num_handles' (60% confidence) (UNUSED)
- Line 198: unused variable 'num_handles' (60% confidence) (UNUSED)

#### gen.py
- Line 118: unused class 'KeyReuseError' (60% confidence) (UNUSED)
- Line 122: unused class 'UnknownKeyError' (60% confidence) (UNUSED)
- Line 126: unused class 'LeakedCallbackError' (60% confidence) (UNUSED)
- Line 134: unused class 'ReturnValueIgnoredError' (60% confidence) (UNUSED)
- Line 557: unused function 'maybe_future' (60% confidence) (UNUSED)

#### http1connection.py
- Line 160: unused attribute '_response_start_line' (60% confidence) (UNUSED)
- Line 206: unused attribute '_response_start_line' (60% confidence) (UNUSED)
- Line 404: unused attribute '_response_start_line' (60% confidence) (UNUSED)

#### httputil.py
- Line 544: unused method 'get_ssl_certificate' (60% confidence) (UNUSED)

#### ioloop.py
- Line 219: unused method 'clear_instance' (60% confidence) (UNUSED)
- Line 833: unused class '_Timeout' (60% confidence) (UNUSED)

#### locale.py
- Line 76: unused function 'set_default_locale' (60% confidence) (UNUSED)
- Line 219: unused function 'get_supported_locales' (60% confidence) (UNUSED)

#### log.py
- Line 196: unused attribute 'end_color' (60% confidence) (UNUSED)
- Line 198: unused attribute 'end_color' (60% confidence) (UNUSED)

#### netutil.py
- Line 317: unreachable code after 'try' (100% confidence) (UNUSED)
- Line 406: unused class 'DefaultExecutorResolver' (60% confidence) (UNUSED)

#### asyncio.py
- Line 362: unused function 'to_tornado_future' (60% confidence) (UNUSED)

#### simple_httpclient.py
- Line 304: unused attribute 'parsed_hostname' (60% confidence) (UNUSED)

#### tcpclient.py
- Line 175: unused method 'clear_timeout' (60% confidence) (UNUSED)

#### asyncio_test.py
- Line 224: unused method 'get_event_loop_on_thread' (60% confidence) (UNUSED)

#### concurrent_test.py
- Line 200: unused attribute '__executor' (60% confidence) (UNUSED)

#### gen_test.py
- Line 364: redundant if-condition (100% confidence) (UNUSED)
- Line 366: unreachable code after 'if' (100% confidence) (UNUSED)
- Line 987: unused attribute '_refcycle' (60% confidence) (UNUSED)
- Line 1022: unused attribute '_refcycle' (60% confidence) (UNUSED)

#### iostream_test.py
- Line 626: unused function 'sleep_some' (60% confidence) (UNUSED)

#### twisted_test.py
- Line 48: unsatisfiable 'if' condition (100% confidence) (UNUSED)
- Line 61: unsatisfiable 'if' condition (100% confidence) (UNUSED)

#### util.py
- Line 73: unused function 'exec_test' (60% confidence) (UNUSED)

#### websocket_test.py
- Line 125: unused attribute 'on_close_called' (60% confidence) (UNUSED)

#### testing.py
- Line 253: unused method '_callTestMethod' (60% confidence) (UNUSED)
- Line 639: unused attribute '__test__' (60% confidence) (UNUSED)

#### web.py
- Line 139: unused variable 'MIN_SUPPORTED_SIGNED_VALUE_VERSION' (60% confidence) (UNUSED)
- Line 147: unused variable 'MAX_SUPPORTED_SIGNED_VALUE_VERSION' (60% confidence) (UNUSED)
- Line 925: unused variable 'get_secure_cookie_key_version' (60% confidence) (UNUSED)
- Line 2296: unused method 'add_transform' (60% confidence) (UNUSED)
- Line 3202: unused class 'FallbackHandler' (60% confidence) (UNUSED)

#### websocket.py
- Line 73: unused class '_WebSocketDelegate' (60% confidence) (UNUSED)
- Line 844: unused attribute '_final_frame' (60% confidence) (UNUSED)
- Line 845: unused attribute '_frame_opcode' (60% confidence) (UNUSED)
- Line 846: unused attribute '_masked_frame' (60% confidence) (UNUSED)
- Line 848: unused attribute '_frame_length' (60% confidence) (UNUSED)
- Line 1164: unused attribute '_frame_length' (60% confidence) (UNUSED)

#### _monitor.py
- Line 33: unused attribute 'woken' (60% confidence) (UNUSED)
- Line 58: unused attribute 'woken' (60% confidence) (UNUSED)

#### __init__.py
- Line 16: unused class 'DummyTqdmFile' (60% confidence) (UNUSED)
- Line 43: unused function 'builtin_iterable' (60% confidence) (UNUSED)

#### logging.py
- Line 99: unused function 'tqdm_logging_redirect' (60% confidence) (UNUSED)

#### dask.py
- Line 28: unused method '_start_state' (60% confidence) (UNUSED)
- Line 32: unused method '_posttask' (60% confidence) (UNUSED)

#### keras.py
- Line 55: unused attribute 'on_epoch_end' (60% confidence) (UNUSED)
- Line 63: unused attribute 'on_batch_end' (60% confidence) (UNUSED)
- Line 67: unused method 'on_train_begin' (60% confidence) (UNUSED)
- Line 73: unused method 'on_epoch_begin' (60% confidence) (UNUSED)
- Line 87: unused attribute 'on_batch_end' (60% confidence) (UNUSED)
- Line 96: unused method 'on_train_end' (60% confidence) (UNUSED)
- Line 112: unused method '_implements_train_batch_hooks' (60% confidence) (UNUSED)
- Line 116: unused method '_implements_test_batch_hooks' (60% confidence) (UNUSED)
- Line 120: unused method '_implements_predict_batch_hooks' (60% confidence) (UNUSED)

#### notebook.py
- Line 19: redundant if-condition (100% confidence) (UNUSED)
- Line 23: unused import 'ipywidgets' (90% confidence) (UNUSED)
- Line 86: unused method '_repr_pretty_' (60% confidence) (UNUSED)
- Line 135: unused attribute 'flex_flow' (60% confidence) (UNUSED)

#### std.py
- Line 125: unused method 'create_th_lock' (60% confidence) (UNUSED)
- Line 925: unused attribute 'progress_apply' (60% confidence) (UNUSED)
- Line 926: unused attribute 'progress_apply' (60% confidence) (UNUSED)
- Line 927: unused attribute 'progress_map' (60% confidence) (UNUSED)
- Line 928: unused attribute 'progress_map' (60% confidence) (UNUSED)
- Line 930: unused attribute 'progress_apply' (60% confidence) (UNUSED)
- Line 931: unused attribute 'progress_apply' (60% confidence) (UNUSED)
- Line 932: unused attribute 'progress_applymap' (60% confidence) (UNUSED)
- Line 933: unused attribute 'progress_map' (60% confidence) (UNUSED)
- Line 934: unused attribute 'progress_map' (60% confidence) (UNUSED)
- Line 937: unused attribute 'progress_apply' (60% confidence) (UNUSED)
- Line 939: unused attribute 'progress_apply' (60% confidence) (UNUSED)
- Line 941: unused attribute 'progress_apply' (60% confidence) (UNUSED)
- Line 942: unused attribute 'progress_aggregate' (60% confidence) (UNUSED)
- Line 943: unused attribute 'progress_transform' (60% confidence) (UNUSED)
- Line 946: unused attribute 'progress_apply' (60% confidence) (UNUSED)
- Line 947: unused attribute 'progress_apply' (60% confidence) (UNUSED)
- Line 949: unused attribute 'progress_apply' (60% confidence) (UNUSED)
- Line 1352: unused method 'unpause' (60% confidence) (UNUSED)
- Line 1382: unused method 'set_description' (60% confidence) (UNUSED)
- Line 1433: unused method 'set_postfix_str' (60% confidence) (UNUSED)
- Line 1500: unused method 'wrapattr' (60% confidence) (UNUSED)

#### tk.py
- Line 143: unused method 'set_description' (60% confidence) (UNUSED)

#### utils.py
- Line 352: unused function '_environ_cols_wrapper' (60% confidence) (UNUSED)

#### typing_extensions.py
- Line 876: unused attribute '__mro_entries__' (60% confidence) (UNUSED)
- Line 1090: unused attribute '__optional_keys__' (60% confidence) (UNUSED)
- Line 1091: unused attribute '__readonly_keys__' (60% confidence) (UNUSED)
- Line 1092: unused attribute '__mutable_keys__' (60% confidence) (UNUSED)
- Line 1094: unused attribute '__closed__' (60% confidence) (UNUSED)
- Line 1095: unused attribute '__extra_items__' (60% confidence) (UNUSED)
- Line 3073: unused attribute '__dataclass_transform__' (60% confidence) (UNUSED)
- Line 3117: unused attribute '__override__' (60% confidence) (UNUSED)
- Line 3551: unused attribute '_field_types' (60% confidence) (UNUSED)

#### __init__.py
- Line 6: unused variable 'IANA_VERSION' (60% confidence) (UNUSED)

#### _collections.py
- Line 15: unused class 'HasGettableStringKeys' (60% confidence) (UNUSED)
- Line 412: unused variable 'getallmatchingheaders' (60% confidence) (UNUSED)

#### connection.py
- Line 993: unused attribute '_peer_cert' (60% confidence) (UNUSED)

#### connectionpool.py
- Line 214: unused attribute 'num_requests' (60% confidence) (UNUSED)
- Line 455: unused attribute 'num_requests' (60% confidence) (UNUSED)
- Line 1163: unused function '_url_from_pool' (60% confidence) (UNUSED)

#### fetch.py
- Line 66: unused variable 'SUCCESS_EOF' (60% confidence) (UNUSED)
- Line 224: unused attribute 'onmessage' (60% confidence) (UNUSED)
- Line 337: unused attribute '_is_done' (60% confidence) (UNUSED)
- Line 364: unused attribute '_is_done' (60% confidence) (UNUSED)
- Line 387: unused attribute '_is_done' (60% confidence) (UNUSED)
- Line 514: unused attribute 'responseType' (60% confidence) (UNUSED)
- Line 703: unused function 'wait_for_streaming_ready' (60% confidence) (UNUSED)

#### pyopenssl.py
- Line 561: unused variable 'err_depth' (100% confidence) (UNUSED)

#### fields.py
- Line 31: unused function 'format_header_param_rfc2231' (60% confidence) (UNUSED)
- Line 135: unused function 'format_header_param' (60% confidence) (UNUSED)

#### poolmanager.py
- Line 64: unused variable 'key_scheme' (60% confidence) (UNUSED)
- Line 65: unused variable 'key_host' (60% confidence) (UNUSED)
- Line 66: unused variable 'key_port' (60% confidence) (UNUSED)
- Line 67: unused variable 'key_timeout' (60% confidence) (UNUSED)
- Line 68: unused variable 'key_retries' (60% confidence) (UNUSED)
- Line 69: unused variable 'key_block' (60% confidence) (UNUSED)
- Line 70: unused variable 'key_source_address' (60% confidence) (UNUSED)
- Line 71: unused variable 'key_key_file' (60% confidence) (UNUSED)
- Line 72: unused variable 'key_key_password' (60% confidence) (UNUSED)
- Line 73: unused variable 'key_cert_file' (60% confidence) (UNUSED)
- Line 74: unused variable 'key_cert_reqs' (60% confidence) (UNUSED)
- Line 75: unused variable 'key_ca_certs' (60% confidence) (UNUSED)
- Line 76: unused variable 'key_ca_cert_data' (60% confidence) (UNUSED)
- Line 77: unused variable 'key_ssl_version' (60% confidence) (UNUSED)
- Line 78: unused variable 'key_ssl_minimum_version' (60% confidence) (UNUSED)
- Line 79: unused variable 'key_ssl_maximum_version' (60% confidence) (UNUSED)
- Line 80: unused variable 'key_ca_cert_dir' (60% confidence) (UNUSED)
- Line 81: unused variable 'key_ssl_context' (60% confidence) (UNUSED)
- Line 82: unused variable 'key_maxsize' (60% confidence) (UNUSED)
- Line 83: unused variable 'key_headers' (60% confidence) (UNUSED)
- Line 84: unused variable 'key__proxy' (60% confidence) (UNUSED)
- Line 85: unused variable 'key__proxy_headers' (60% confidence) (UNUSED)
- Line 86: unused variable 'key__proxy_config' (60% confidence) (UNUSED)
- Line 87: unused variable 'key_socket_options' (60% confidence) (UNUSED)
- Line 88: unused variable 'key__socks_options' (60% confidence) (UNUSED)
- Line 89: unused variable 'key_assert_hostname' (60% confidence) (UNUSED)
- Line 90: unused variable 'key_assert_fingerprint' (60% confidence) (UNUSED)
- Line 91: unused variable 'key_server_hostname' (60% confidence) (UNUSED)
- Line 92: unused variable 'key_blocksize' (60% confidence) (UNUSED)

#### ssl_.py
- Line 85: unused variable 'subjectAltName' (60% confidence) (UNUSED)
- Line 87: unused variable 'serialNumber' (60% confidence) (UNUSED)

#### __init__.py
- Line 62: unused function 'compose_all' (60% confidence) (UNUSED)
- Line 97: unused function 'full_load' (60% confidence) (UNUSED)
- Line 107: unused function 'full_load_all' (60% confidence) (UNUSED)
- Line 127: unused function 'safe_load_all' (60% confidence) (UNUSED)
- Line 137: unused function 'unsafe_load' (60% confidence) (UNUSED)
- Line 147: unused function 'unsafe_load_all' (60% confidence) (UNUSED)
- Line 255: unused function 'safe_dump_all' (60% confidence) (UNUSED)
- Line 362: unused class 'YAMLObject' (60% confidence) (UNUSED)

#### constructor.py
- Line 147: unused method 'construct_pairs' (60% confidence) (UNUSED)

#### emitter.py
- Line 65: unused attribute 'sequence_context' (60% confidence) (UNUSED)
- Line 235: unused attribute 'sequence_context' (60% confidence) (UNUSED)
- Line 703: unused variable 'unicode_characters' (60% confidence) (UNUSED)

#### code-quality-checker-streamlit.py
- Line 80: unused function 'parse_pylint' (60% confidence) (UNUSED)
- Line 98: unused function 'parse_mypy' (60% confidence) (UNUSED)
- Line 116: unused function 'parse_bandit' (60% confidence) (UNUSED)
- Line 134: unused function 'parse_flake8' (60% confidence) (UNUSED)
- Line 152: unused function 'parse_vulture' (60% confidence) (UNUSED)

### flake8 (✅ Helps with readability)
Keeps formatting, line breaks, and indentations clean

*No issues found.*

## Recommendations
Based on the analysis, consider these Streamlit-specific best practices:

1. **Widget Duplication**: Always use unique `key` parameters for interactive elements
2. **State Management**: Properly initialize `session_state` variables before use
3. **Form Handling**: Keep form widgets and submission handling together
4. **Execution Flow**: Remember Streamlit reruns the entire script on each interaction
5. **Type Safety**: Add type hints to improve readability and catch errors early