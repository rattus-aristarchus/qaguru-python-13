from selene import browser, have, command
import allure


class RegistrationPage:

    @allure.step("Открываем страницу")
    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    @allure.step("Регистрируем пользователя")
    def register(self, user):
        self._set_name(user.name)
        self._set_last_name(user.last_name)
        self._set_email(user.email)

        # fill in the basic stuff

        self._set_gender(user.gender)
        self._set_number(user.number)
        self._set_birthday(user.date_of_birth)

        # fill in the hobbies
        self._add_interest(user.subjects[0])
        self._add_interest(user.subjects[1])
        self._add_hobby(user.hobbies[0])
        self._add_hobby(user.hobbies[1])

        # fill in the full address
        self._set_address(user.address)
        self._set_state(user.state)
        self._set_city(user.city)

        self._submit()

    @allure.step("Убеждаемся, что пользователь существует")
    def should_have_user(self, user):
        self._should_have_user_fields(user.name,
                                      user.last_name,
                                      user.email,
                                      user.gender,
                                      user.number,
                                      user.date_of_birth_str,
                                      user.subjects_str,
                                      user.hobbies_str,
                                      user.address,
                                      user.state,
                                      user.city)

    def _set_name(self, name):
        browser.element("#firstName").type(name)

    def _set_last_name(self, last_name):
        browser.element("#lastName").type(last_name)

    def _set_gender(self, gender):
        if gender == "Female":
            browser.element('[for="gender-radio-2"]').click()
        elif gender == "Male":
            browser.element('[for="gender-radio-1"]').click()

    def _set_number(self, number):
        browser.element("#userNumber").type(number)

    def _set_email(self, email):
        browser.element("#userEmail").type(email)

    def _set_birthday(self, date_of_birth):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type(date_of_birth.strftime("%Y"))
        browser.element(".react-datepicker__month-select").type(date_of_birth.strftime("%B"))
        browser.element(
            f".react-datepicker__day.react-datepicker__day--00{date_of_birth.day}"
        ).click()

    def _add_interest(self, subject):
        browser.element("#subjectsInput").type(subject).press_enter()

    def _add_hobby(self, hobby):
        if hobby == "Sports":
            browser.element('[for="hobbies-checkbox-1"]').click()
        elif hobby == "Reading":
            browser.element('[for="hobbies-checkbox-2"]').click()
        elif hobby == "Music":
            browser.element('[for="hobbies-checkbox-3"]').click()

    def _set_address(self, address):
        browser.element("#currentAddress").type(address)

    def _set_state(self, state):
        browser.element("#react-select-3-input").type(state).press_enter()

    def _set_city(self, city):
        browser.element("#react-select-4-input").type(city).press_enter()

    def _submit(self):
        browser.element("#submit").press_enter()

    def _should_have_user_fields(self, *args):
        for arg in args:
            browser.element(".table").should(have.text(arg))
