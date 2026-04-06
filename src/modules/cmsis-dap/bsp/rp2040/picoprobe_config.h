/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2021 Raspberry Pi (Trading) Ltd.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 */

#include <stdint.h>

#ifndef PICOPROBE_H_
#define PICOPROBE_H_

// PIO config
#define PROBE_SM 0
// #define PROBE_PIN_SWCLK 10 // changes made to choose SWD pins of our choice
// #define PROBE_PIN_SWDIO 11 // 
extern uint32_t PROBE_PIN_SWCLK;
extern uint32_t PROBE_PIN_SWDIO;
extern uint32_t PROBE_PIN_TDI;
extern uint32_t PROBE_PIN_TDO;

// UART config
#define PICOPROBE_UART_TX 0
#define PICOPROBE_UART_RX 1
#define PICOPROBE_UART_INTERFACE uart0
#define PICOPROBE_UART_BAUDRATE 115200

// LED config
#define PICOPROBE_LED 24

void cmsisDapSetPins(uint32_t swclk, uint32_t swdio);
void cmsisDapSetJTAGPins(uint32_t tck, uint32_t tms, uint32_t tdi, uint32_t tdo);

#endif
