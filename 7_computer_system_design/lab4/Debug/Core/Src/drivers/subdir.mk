################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Src/drivers/pins.c \
../Core/Src/drivers/uart_blocking_driver.c \
../Core/Src/drivers/uart_interrupt_driver.c 

OBJS += \
./Core/Src/drivers/pins.o \
./Core/Src/drivers/uart_blocking_driver.o \
./Core/Src/drivers/uart_interrupt_driver.o 

C_DEPS += \
./Core/Src/drivers/pins.d \
./Core/Src/drivers/uart_blocking_driver.d \
./Core/Src/drivers/uart_interrupt_driver.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/drivers/%.o Core/Src/drivers/%.su: ../Core/Src/drivers/%.c Core/Src/drivers/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F427xx -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src-2f-drivers

clean-Core-2f-Src-2f-drivers:
	-$(RM) ./Core/Src/drivers/pins.d ./Core/Src/drivers/pins.o ./Core/Src/drivers/pins.su ./Core/Src/drivers/uart_blocking_driver.d ./Core/Src/drivers/uart_blocking_driver.o ./Core/Src/drivers/uart_blocking_driver.su ./Core/Src/drivers/uart_interrupt_driver.d ./Core/Src/drivers/uart_interrupt_driver.o ./Core/Src/drivers/uart_interrupt_driver.su

.PHONY: clean-Core-2f-Src-2f-drivers

