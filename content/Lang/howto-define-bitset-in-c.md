---
Title: 如何用C语言定义Bitset（位集）
Tags: c
Category: 语言
Date: 2014-11-03 13:53
Slug: how-to-define-bitset-in-c
Subtitle: 
Summary: 
Keywords:
---

```C
#define DECLARE_BITSET(__bs, __width) uint8_t __bs[((__width - 1) >> 3) + 1]

#define BITSET_SET_BIT(__bs, __pos)    ((__bs)[(__pos) >> 3] |= (1 << ((__pos) & 0x07)))
#define BITSET_UNSET_BIT(__bs, __pos)  ((__bs)[(__pos) >> 3] &= ~(1 << ((__pos) & 0x07)))
#define BITSET_IS_BIT_SET(__bs,__pos)  ((__bs)[(__pos) >> 3] & (1 << ((__pos) & 0x07)))
#define BITSET_CLEAR(__bs, __width)    (memset(__bs, 0, (((__width - 1) >> 3) + 1) * sizeof(uint8_t)))
#define BITSET_IS_ZEROS(__bs, __width) __BITSET_IS_ZEROS((uint8_t *)(__bs), __width)

static inline int __BITSET_IS_ZEROS(uint8_t *bs, size_t size)
{
    size_t i;

    for (i = 0; i < size; i++) {
        if (bs[i] != 0) {
            return FALSE;
        }
    }
    return TRUE;
}
```