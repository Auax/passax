import React, { useState } from "react";
import Code, { copyToClipboard } from "./MarkupCode";
import { Toaster } from "react-hot-toast";
import * as vars_ from "./Variables";

const Home = () => {
    // UseState to change the theme
    const [theme, setTheme] = useState("dark");

    // UseState to open and close menu
    const [navbarOpen, setNavbarOpen] = React.useState(false);

    // Get <pre> element(s)
    let codePreElements = document.getElementsByClassName("code-pre");

    const toggleCodeOpacity = (theme_) => {
        // Change background opacity
        for (let i = 0; i < codePreElements.length; i++) {
            let pre = codePreElements[i];
            pre.style.backgroundColor =
                theme_ === "dark"
                    ? "rgba(24, 24, 24, 0.65)"
                    : "rgb(24, 24, 24)";
        }
    };

    const toggleDarkMode = () => {
        let root = document.getElementsByTagName("html")[0];
        let theme = root.getAttribute("class");
        let class_ = theme === "dark" ? "light" : "dark";
        root.setAttribute("class", class_);
        // Change useState
        setTheme(class_);

        // Change background opacity
        toggleCodeOpacity(class_);
    };

    window.onload = () => {
        toggleCodeOpacity(theme);
    };

    return (
        <div className="Home dark:bg-c-dark-blue bg-slate-200">

            <Toaster />

            <div className={theme === "dark" ? "hero-dark" : "hero-light"}>
                <nav className="bg-white dark:bg-c-dark-blue border-gray-200 px-2 sm:px-4 py-2.5">
                    <div className="flex flex-wrap justify-between items-center mx-auto">
                        <a href="#" className="flex">
                            {/* You can add a logo here with: mr-3 h-10*/}
                            <span
                                className="self-center text-lg font-semibold
                            whitespace-nowrap text-black dark:text-white"
                            >
                                Auax
                            </span>
                        </a>

                        <button
                            onClick={() => setNavbarOpen(!navbarOpen)}
                            type="button"
                            className="inline-flex items-center p-2 ml-3 text-sm text-gray-500
                                 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none
                                 focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                            aria-controls="mobile-menu-2"
                            aria-expanded="false"
                        >
                            <span className="sr-only">Open main menu</span>
                            <svg
                                className="w-6 h-6"
                                fill="currentColor"
                                viewBox="0 0 20 20"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                    fillRule="evenodd"
                                    d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                                    clipRule="evenodd"
                                />
                            </svg>
                            <svg
                                className="hidden w-6 h-6"
                                fill="currentColor"
                                viewBox="0 0 20 20"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                    fillRule="evenodd"
                                    d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                                    clipRule="evenodd"
                                />
                            </svg>
                        </button>
                        <div
                            className={
                                "w-full md:block md:w-auto " +
                                (navbarOpen ? "" : "hidden")
                            }
                            id=""
                        >
                            <ul className="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium">
                                <li className="my-auto">
                                    <a
                                        href="https://github.com/Auax/passax"
                                        target="_blank"
                                        className="navbar-link"
                                        aria-current="page"
                                    >
                                        GitHub
                                    </a>
                                </li>
                                <li className="my-auto">
                                    <a
                                        href="https://pypi.org/project/passax"
                                        target="_blank"
                                        className="navbar-link"
                                        aria-current="page"
                                    >
                                        PYPI
                                    </a>
                                </li>
                                <li>
                                    <button
                                        className="btn btn-square btn-ghost bg-zinc-50/5 md:bg-transparent my-auto
                                        w-full md:w-auto h-full min-h-0 px-2 normal-case rounded-none md:rounded-lg hover:scale-105"
                                        onClick={() => toggleDarkMode()}
                                    >
                                        <span
                                            className="text-black dark:text-white items-center inline-flex min-h-12 h-12
                                            md:bg-transparent md:text-blue-700 md:p-0 dark:text-white block md:hidden"
                                        >
                                            Theme:
                                        </span>
                                        <div
                                            className={
                                                "icon min-h-full mt-1 " +
                                                (navbarOpen ? "ml-2 mb-1" : "")
                                            }
                                        >
                                            {theme === "dark"
                                                ? vars_.dark_icon
                                                : vars_.light_icon}
                                        </div>
                                    </button>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>

                {/*Hero section*/}
                <div className="container mx-auto flex flex-col">
                    {/*Title and subtitle*/}
                    <h1 className="text-5xl sm:text-6xl font-bold text-center dark:text-slate-200 text-stone-900 mt-32 sm:mt-40 px-9 sm:px-0 tracking-tight">
                        A library to retrieve <br />
                        Chromium browsers login data.
                    </h1>
                    <p className="text-lg font-medium text-center dark:text-gray-400 text-zinc-600 mt-4 px-20 sm:px-0">
                        This Python3 library allows you to quickly retrieve all
                        the passwords for browsers like
                        <span className="dark:text-cyan-500 text-cyan-700">
                            {" "}
                            Chrome
                        </span>{" "}
                        or
                        <span className="dark:text-cyan-500 text-cyan-700">
                            {" "}
                            Opera
                        </span>
                        .
                    </p>

                    <div
                        className="flex flex-col items-center justify-center w-full
                    space-y-2 lg:space-x-4 lg:space-y-0 lg:flex-row mt-14 mb-20"
                    >
                        <div className="flex flex-col max-w-sm gap-2 mt-2">
                            <h1 className="text-3xl font-bold tracking-tight lg:ml-auto dark:text-slate-200 text-stone-900">
                                Installation
                            </h1>
                            <p className="text-lg font-medium dark:text-gray-400 ml-auto text-zinc-600">
                                Python3 or superior is required!
                            </p>
                        </div>

                        {/*Markup code*/}
                        <div
                            onClick={() =>
                                copyToClipboard("pip install passax")
                            }
                            className="flex-1 w-full max-w-xs text-left bg-slate-900/70 dark:hover:bg-slate-900/50 hover:bg-slate-900/75
                             transition ease-in-out border-2 text-primary-content border-opacity-40
                             dark:border-primary-content/10 border-primary/0 mockup-code lg:mx-0 cursor-pointer"
                        >
                            <pre className="animate-pulse" data-prefix="$">
                                <code>pip install passax</code>
                            </pre>
                        </div>
                    </div>
                </div>
            </div>

            {/*Code examples*/}
            <div className="code-examples-container container mx-auto">
                <h1 className="text-2xl sm:text-3xl font-bold mt-20 px-9 sm:px-0 tracking-tight sm:text-center dark:text-slate-200 text-stone-900">
                    Try the library now with these code examples!
                </h1>

                {/*First code example*/}
                <p className="mt-10 px-10 tracking-tight dark:text-gray-400 text-stone-800">
                    Print to screen the login info from Chrome:
                </p>
                <Code text={vars_.exampleCode1} />

                {/*Second code example*/}
                <p className="mt-16 px-10 tracking-tight dark:text-gray-400 text-stone-800">
                    Save login data from all supported browsers:
                </p>
                <Code text={vars_.exampleCode2} />

                {/*Third code example*/}
                <div className="mb-20">
                    <p className="mt-16 px-10 tracking-tight dark:text-gray-400 text-stone-800">
                        Run in any supported OS:
                    </p>
                    <Code text={vars_.exampleCode3} />
                </div>
            </div>

            {/*Footer*/}
            <footer className="p-10 footer bg-base-200 text-base-content footer-center h-full">
                <div>
                    <p>Copyright © 2022 - All right reserved by Auax</p>
                </div>
            </footer>
        </div>
    );
};

export default Home;
